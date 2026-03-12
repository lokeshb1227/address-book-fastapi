# Address Book API – FastAPI

## Overview

This project is a simple Address Book REST API built using FastAPI and SQLite.
The goal of this service is to allow users to store and manage address records with geographical coordinates (latitude and longitude).

The API supports basic CRUD operations like creating, updating and deleting addresses, and also provides an endpoint to fetch nearby addresses based on a given location.

This project was implemented as a lightweight backend service using FastAPI because of its simplicity, speed, and automatic API documentation.

---

## Tech Stack

* Python 3
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn (ASGI server)

---

## Features

* Create a new address record
* Update an existing address
* Delete an address
* Retrieve all stored addresses
* Find nearby addresses using coordinates
* Auto-generated API documentation via Swagger UI

---

## Project Structure

```
address-book-fastapi
│
├── main.py        # FastAPI application
└── README.md      # Project documentation
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/address-book-fastapi.git
```

### 2. Navigate to the project directory

```
cd address-book-fastapi
```

### 3. Install required dependencies

```
pip install fastapi uvicorn sqlalchemy
```

### 4. Run the application

```
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

From here you can test all endpoints directly.

---

## Available Endpoints

**POST /addresses**
Create a new address entry.

**GET /addresses**
Fetch all stored addresses.

**PUT /addresses/{address_id}**
Update an existing address.

**DELETE /addresses/{address_id}**
Delete an address from the system.

**GET /addresses/nearby**
Retrieve addresses within a given distance from specified coordinates.

---

## Example Request Body

```
{
  "name": "Home",
  "latitude": 12.9716,
  "longitude": 77.5946
}
```

---

## Notes

* SQLite is used as a lightweight local database for simplicity.
* FastAPI’s automatic validation through Pydantic ensures valid request data.
* Swagger UI is used for quick testing and documentation of endpoints.

---

## Future Improvements

Some improvements that could be added later:

* Authentication for API access
* Pagination for address listing
* Using a production database like PostgreSQL
* Implementing Haversine formula for more accurate distance calculation

---

## Author

Lokesh
