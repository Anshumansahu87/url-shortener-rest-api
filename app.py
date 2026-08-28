from flask import Flask, request, jsonify, redirect
import sqlite3
import string
import secrets
from datetime import datetime

app = Flask(__name__)
DB_NAME = "urls.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL,
            clicks INTEGER DEFAULT 0,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json(silent=True) or {}
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "url is required"}), 400

    conn = get_db()

    # Reuse existing mapping when the same URL already exists.
    existing = conn.execute(
        "SELECT * FROM urls WHERE original_url = ?",
        (original_url,)
    ).fetchone()

    if existing:
        result = dict(existing)
        conn.close()
        return jsonify({
            "message": "URL already shortened",
            "short_code": result["short_code"],
            "short_url": f"http://localhost:5000/{result['short_code']}"
        })

    while True:
        code = generate_code()
        try:
            conn.execute(
                "INSERT INTO urls (original_url, short_code, created_at) VALUES (?, ?, ?)",
                (original_url, code, datetime.now().isoformat(timespec="seconds"))
            )
            conn.commit()
            break
        except sqlite3.IntegrityError:
            continue

    conn.close()

    return jsonify({
        "message": "URL shortened successfully",
        "short_code": code,
        "short_url": f"http://localhost:5000/{code}"
    }), 201

@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()

    if not row:
        conn.close()
        return jsonify({"error": "Short URL not found"}), 404

    conn.execute(
        "UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?",
        (short_code,)
    )
    conn.commit()
    conn.close()

    return redirect(row["original_url"])

@app.route("/api/url/<short_code>", methods=["GET"])
def get_url(short_code):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()
    conn.close()

    if not row:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify(dict(row))

@app.route("/api/urls", methods=["GET"])
def get_all_urls():
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM urls ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return jsonify([dict(row) for row in rows])

@app.route("/api/url/<short_code>", methods=["DELETE"])
def delete_url(short_code):
    conn = get_db()
    cursor = conn.execute(
        "DELETE FROM urls WHERE short_code = ?",
        (short_code,)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify({"message": "URL deleted successfully"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
