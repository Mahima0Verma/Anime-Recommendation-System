   # Anime Recommendation System API

This project is a Django REST Framework-based API that integrates with the AniList GraphQL API to provide anime search functionality, personalized recommendations, and user preference management.

## Features
- **User Authentication:** User registration and login using JWT tokens.
- **Anime Search:** Search for anime by name or genre using the AniList API.
- **User Preferences:** Save and manage user preferences such as favorite genres and watched anime.
- **Anime Recommendations:** Get personalized anime recommendations based on user preferences.

---

## Setup and Run Locally

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL


### Installation Steps

1. Create a virtual environment and activate it:
   ```bash
  - python -m venv env #for creation of virtual environment in window
  - source env/Scripts/activate  #for activation of virtual environment in window

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Set up your environment variables: Create a .env file in the project root and configure the following:

```bash
 DB_NAME=
 DB_USER=
 DB_PASSWORD=
 DB_HOST=
 DB_PORT=

4. Apply migrations:

   ```bash
   python manage.py migrate

5. Run the development server:

   ```bash
   python manage.py runserver


### Endpoints
### Authentication
1. Register
### URL
POST /auth/register

## Request Body:
```json
      {
       "email": "user@example.com",
       "name": "John Doe",
       "password": "yourpassword",
       "password2": "yourpassword"
      }
```
## Response:
```json
   {
       "MSG": "User registration complete."
   }
```
## Login
   ```json
   URL: POST /auth/login
```
## Request Body:
   ```json
   {
       "email": "user@example.com",
       "password": "yourpassword"
   }
```
## Response:

```json
{
    "token": {
        "refresh": "refresh_token",
        "access": "access_token"
    },
    "msg": "login successful"
}
```
## Anime Search
## URL: 
GET /anime/search
## Query Parameters:

- name (optional): Search anime by name.
- genre (optional): Filter anime by genre.
## Example Request:
GET /anime/search?name=Naruto

## Response:

```json
[
    {
        "id": 123,
        "title": {
            "romaji": "Naruto"
        },
        "description": "A story about a young ninja...",
        "genres": ["Action", "Adventure"]
    }
]
```
## User Preferences
## Get Preferences
## URL: 
GET /user/preferences
## Headers:

## Authorization: Bearer access_token
## Response:
```json
{
    "favorite_genres": "Action,Adventure",
    "watched_anime": "123,456"
}
```
## Set Preferences
## URL: 
POST /user/preferences
## Headers:
## Authorization: Bearer access_token
## Request Body:
```json
{
    "favorite_genres": "Comedy,Drama",
    "watched_anime": "789,1011"
}
```
## Response:

```json
{
    "favorite_genres": "Comedy,Drama",
    "watched_anime": "789,1011"
}
```
## Anime Recommendations
## URL: 
GET /anime/recommendations
## Headers:

## Authorization: Bearer access_token
## Response:

```json
[
    {
        "id": 567,
        "title": {
            "romaji": "One Piece"
        },
        "description": "A story about pirates...",
        "genres": ["Action", "Adventure"]
    }
]
```



