# VerveBridge_ContentManagementSystem_Task

# Content Management System (CMS) Backend

This project is a Content Management System (CMS) developed using Django for the backend. The CMS allows users to manage dynamic content across various frontend pages, such as `index`, `contact`, `team`, `testimonial`, `about`, `menu`, `booking`, and `service`. Users can perform CRUD operations (Create, Read, Update, Delete) on the content through a RESTful API. User authentication and role-based access control ensure that only authorized users can manage content.

## Features

- User authentication (JWT-based).
- RESTful API for managing content.
- CRUD operations for pages.
- Admin panel for content management.
- Secure authentication and access control.
- Frontend integration with dynamic content rendering.

## Prerequisites

Before running the project, ensure that you have the following installed:

- **Python 3.x**
- **MySQL** (or any compatible database)
- **Django 4.x**
- **pip** (Python package manager)

## Setup and Installation

1. Clone the Repository

```bash
git clone https://github.com/your-username/vervebridge-cms-backend.git
cd vervebridge-cms-backend

2. Create a Virtual Environment

python3 -m venv env
`env\Scripts\activate`  # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Configure the Database

Create a MySQL database called test_cms_db.
Update the DATABASES configuration in settings.py to match your MySQL setup:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_cms_db',
        'USER': 'username',  # Your MySQL username
        'PASSWORD': 'password',  # Your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Apply the migrations to set up the database schema:
python manage.py migrate

5. Run the Development Server

python manage.py runserver
The API will be available at http://localhost:8000/


### API Endpoints

Authentication
    Login (Get JWT Token):
      POST /api/token/
      Example body:
      json
      {
          "username": "your_username",
          "password": "your_password"
      }

    Refresh Token:
      POST /api/token/refresh/

Pages API
    List All Pages: GET /api/pages/
    Create a Page: POST /api/pages/
    Retrieve a Specific Page: GET /api/pages/<id>/
    Update a Page: PUT /api/pages/<id>/
    Delete a Page: DELETE /api/pages/<id>/

    Example API Request (Using JWT Token)
    Include the JWT token in the Authorization header for protected routes:
      GET /api/pages/
      Authorization: Bearer <your_access_token>


#### Running Tests
  To run tests, execute the following command:
    python manage.py test


#### Admin Panel
  Django provides an admin panel for managing content and users. To access the admin panel:
    Create a superuser:
      python manage.py createsuperuser
      Visit the admin interface at http://localhost:8000/admin/





#### Project Structure:
vervebridge-cms-backend/
│
├── content_management/  # Django app containing models, views, and APIs
├── tests.py             # Test cases for the API
├── manage.py            # Django project management script
├── requirements.txt     # Project dependencies
└── README.md          
