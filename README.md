# URL Shortener REST API

A beginner-friendly backend project built with **Python, Flask, SQLite and REST APIs**.

## Features

- Generate unique short URLs
- Redirect short URLs to original URLs
- Track click counts
- Get URL details
- List all shortened URLs
- Delete a shortened URL
- Health-check endpoint

## Project Structure

```text
url-shortener-backend/
├── app.py
├── requirements.txt
├── README.md
└── urls.db              # created automatically after first run
```

## Run Locally

### 1. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the server

```bash
python app.py
```

The API runs at:

```text
http://localhost:5000
```

## API Testing

### Create Short URL

**POST** `/api/shorten`

JSON:

```json
{
  "url": "https://github.com/"
}
```

Example response:

```json
{
  "message": "URL shortened successfully",
  "short_code": "a8K2xQ",
  "short_url": "http://localhost:5000/a8K2xQ"
}
```

### Redirect

Open:

```text
http://localhost:5000/a8K2xQ
```

The browser redirects to the original URL.

### Get URL Details

**GET**

```text
/api/url/a8K2xQ
```

### List All URLs

**GET**

```text
/api/urls
```

### Delete URL

**DELETE**

```text
/api/url/a8K2xQ
```

### Health Check

**GET**

```text
/health
```

## Interview Concepts Covered

- REST API
- HTTP methods: GET, POST, DELETE
- JSON
- CRUD operations
- SQLite and SQL
- Unique IDs
- Database queries
- URL redirection
- Click tracking
- Error handling
- Git/GitHub workflow

## Resume Bullet Points

**URL Shortener REST API | Python, Flask, SQLite**

- Developed a REST API to generate unique short URLs from long URLs and redirect users to original links.
- Implemented CRUD operations and click tracking using Flask and SQLite.
- Designed database operations for URL mapping, access counts and creation timestamps.
- Tested API endpoints using Postman and documented the project for GitHub.
