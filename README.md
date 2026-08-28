# URL Shortener REST API

A beginner-friendly backend project built with **Python, Flask, SQLite, and REST APIs**.

The application converts long URLs into short unique links and redirects users to the original URL. It also tracks how many times each short URL has been accessed.

## Features

- Generate unique short URLs
- Redirect short URLs to original URLs
- Track click counts
- Get details of a shortened URL
- List all shortened URLs
- Delete shortened URLs
- Health-check endpoint
- SQLite database storage
- REST API with JSON responses

## Tech Stack

- **Language:** Python
- **Backend:** Flask
- **Database:** SQLite
- **API:** REST API
- **Testing:** Postman
- **Version Control:** Git & GitHub

## Project Structure

```text
url-shortener-rest-api/
├── app.py
├── requirements.txt
├── README.md
├── postman_examples.txt
├── .gitignore
└── urls.db              # created automatically when the app runs
```

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Anshumansahu87/url-shortener-rest-api.git
cd url-shortener-rest-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the server

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/shorten` | Create a short URL |
| GET | `/<short_code>` | Redirect to the original URL |
| GET | `/api/url/<short_code>` | Get URL details and click count |
| GET | `/api/urls` | Get all shortened URLs |
| DELETE | `/api/url/<short_code>` | Delete a shortened URL |
| GET | `/health` | Check API status |

## API Usage

### 1. Create a Short URL

**POST**

```text
http://127.0.0.1:5000/api/shorten
```

Request body:

```json
{
  "url": "https://github.com/"
}
```

Example response:

```json
{
  "message": "URL shortened successfully",
  "short_code": "rtYUPP",
  "short_url": "http://localhost:5000/rtYUPP"
}
```

### 2. Redirect to Original URL

Open the generated short URL in a browser:

```text
http://127.0.0.1:5000/rtYUPP
```

The application redirects to the original URL.

### 3. Get URL Details

**GET**

```text
http://127.0.0.1:5000/api/url/rtYUPP
```

Example response:

```json
{
  "clicks": 2,
  "created_at": "2026-08-28T21:16:46",
  "id": 1,
  "original_url": "https://github.com/",
  "short_code": "rtYUPP"
}
```

### 4. Get All URLs

**GET**

```text
http://127.0.0.1:5000/api/urls
```

### 5. Delete a Short URL

**DELETE**

```text
http://127.0.0.1:5000/api/url/rtYUPP
```

### 6. Health Check

**GET**

```text
http://127.0.0.1:5000/health
```

Example response:

```json
{
  "status": "ok"
}
```

## Testing with Postman

1. Start the Flask server using `python app.py`.
2. Open Postman.
3. Use `POST /api/shorten` to create a short URL.
4. Use `GET /api/url/<short_code>` to check URL details and click count.
5. Use `DELETE /api/url/<short_code>` to remove a URL.

Sample requests are also available in `postman_examples.txt`.

## Database

The project uses SQLite.

The database file `urls.db` is created automatically when the application starts.

The `urls` table stores:

- URL ID
- Original URL
- Short code
- Click count
- Creation timestamp

## Backend Concepts Demonstrated

- REST API development
- HTTP methods: GET, POST, DELETE
- JSON request and response handling
- CRUD-style URL management
- SQLite database operations
- SQL queries
- Unique short-code generation
- URL redirection
- Click tracking
- Error handling
- Git and GitHub workflow
- API testing with Postman

## Future Improvements

- Add user authentication
- Add URL expiration
- Add custom short codes
- Add URL validation
- Add automated unit tests
- Add a frontend interface
- Deploy the API to a cloud platform

## Resume Description

**URL Shortener REST API | Python, Flask, SQLite**

- Developed a REST API to generate unique short URLs and redirect users to original links.
- Implemented URL management operations and click tracking using Flask and SQLite.
- Designed database operations for URL mapping, access counts, and creation timestamps.
- Tested REST API endpoints using Postman and documented the project on GitHub.
