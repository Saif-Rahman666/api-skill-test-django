API Developer Skill Test - Simple RESTful CRUD API (Django REST Framework)
This project implements a basic RESTful API using Python, Django, and Django REST Framework (DRF). It demonstrates standard CRUD (Create, Read, Update, Delete) operations for a "Product" resource, utilizing Django's ORM and an SQLite in-memory-like database (default for Django development).

Project Structure
.
├── manage.py        # Django's command-line utility
├── myproject/       # Main Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py  # Project settings
│   ├── urls.py      # Main URL configuration
│   └── wsgi.py
├── products_api/    # Django app for product API logic
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py    # Product database model
│   ├── serializers.py # Data serialization/deserialization logic
│   ├── tests.py
│   ├── urls.py      # App-specific URL patterns
│   └── views.py     # API ViewSet for CRUD operations
├── venv/            # Python Virtual Environment
├── db.sqlite3       # Default SQLite database file (created after migrations)
└── README.md        # This file

Features
Resource: Product

Data Store: SQLite (default Django database backend, behaves like an in-memory store for this task as it's a simple file-based database that rebuilds on migrate).

Backend: Python 3.x, Django, Django REST Framework.

Endpoints:

POST /api/products/: Create a new product.

GET /api/products/: Retrieve all products.

GET /api/products/:id/: Retrieve a single product by ID.

PUT /api/products/:id/: Update an existing product by ID.

DELETE /api/products/:id/: Delete a product by ID.

Error Handling: DRF automatically handles 404 Not Found for non-existent IDs and 400 Bad Request for invalid input (via serializer validation).

HTTP Status Codes: Correctly uses 200 OK, 201 Created, 204 No Content, 400 Bad Request, 404 Not Found.

Code Quality: Follows Django and DRF best practices, with clear modularization and comments.

Setup and Run Instructions
To get this API running on your local machine, follow these steps:

Clone the Repository:

git clone <[https://github.com/Saif-Rahman666/api-skill-test-django.git]>
cd api-skill-test-django

Create and Activate a Virtual Environment:

python -m venv env
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

Install Dependencies:

pip install django djangorestframework

Apply Database Migrations:
This creates the necessary database tables based on the Product model.

python manage.py makemigrations products_api
python manage.py migrate

Run the Django Development Server:

python manage.py runserver

The server will start, typically on http://127.0.0.1:8000/.

API Usage Examples
The API will be accessible at http://127.0.0.1:8000/api/. Django REST Framework also provides a Browsable API at these URLs, allowing you to interact directly via your web browser.

Base URL for Products: http://127.0.0.1:8000/api/products/

1. Create a Product (POST)

Endpoint: POST http://127.0.0.1:8000/api/products/

Headers: Content-Type: application/json

Body (JSON):

{
    "name": "Wireless Headphones",
    "price": 79.99,
    "description": "Noise-cancelling headphones for immersive audio."
}

Expected Response: 201 Created with the new product object.

2. Retrieve All Products (GET)

Endpoint: GET http://127.0.0.1:8000/api/products/

Expected Response: 200 OK with an array of product objects.

3. Retrieve a Single Product by ID (GET)

(Replace 1 with an actual product ID obtained from a POST or GET all request)

Endpoint: GET http://127.0.0.1:8000/api/products/1/

Expected Response: 200 OK with the product object if found, or 404 Not Found if not.

4. Update a Product by ID (PUT)

(Replace 1 with an actual product ID)

Endpoint: PUT http://127.0.0.1:8000/api/products/1/

Headers: Content-Type: application/json

Body (JSON):

{
    "name": "Updated Wireless Headphones Pro",
    "price": 99.99,
    "description": "Premium noise-cancelling headphones with enhanced bass."
}

Expected Response: 200 OK with the updated product object if found, or 404 Not Found if not.

5. Delete a Product by ID (DELETE)

(Replace 1 with an actual product ID)

Endpoint: DELETE http://127.0.0.1:8000/api/products/1/

Expected Response: 204 No Content if successful, or 404 Not Found if not.


Postman Sample Screenshots

