
# Content Management System (CMS) API

A Django-based API for managing and organizing content, supporting key CMS features like user management, content categorization, and content metadata.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The CMS API provides a backend solution for managing content. It supports typical CMS functionalities like handling users, categorizing content, and managing permissions. This project is ideal for those looking to integrate a CMS backend with their front-end applications.

## Features

- **User Authentication**: Register, login, and manage users securely.
- **Content Management**: Create, read, update, and delete content.
- **Categorization**: Organize content by categories, tags, and metadata.
- **Admin Dashboard**: Admin-level capabilities for content and user management.
- **Validation and Security**: Custom validation rules and secure API endpoints.

## Installation

1. **Clone the Repository**

   git clone https://github.com/charan19061998/content_management.git
   cd content_management

2. **Create a Virtual Environment**

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

   pip install -r requirements.txt

4. **Set Up the Database**

   Apply migrations to set up the database:

   python manage.py migrate

5. **Run the Development Server**

   python manage.py runserver

## Usage

- **Admin Interface**: Visit `http://127.0.0.1:8000/admin` for the Django admin panel.
- **API Testing**: You can use tools like Postman or cURL to test API endpoints.

## API Endpoints

### Authentication

- **POST** `/api/auth/register/`: Register a new user.
- **POST** `/api/auth/login/`: Authenticate a user and return a token.

### Content Management

- **GET** `/api/content/`: List all content items.
- **POST** `/api/content/`: Create a new content item.
- **GET** `/api/content/<id>/`: Retrieve details of a specific content item.
- **PUT** `/api/content/<id>/`: Update an existing content item.
- **DELETE** `/api/content/<id>/`: Delete a content item.

### Categories and Tags

- **GET** `/api/categories/`: List all categories.
- **POST** `/api/categories/`: Create a new category.

## Contributing

Contributions are welcome! Please open issues and pull requests as needed.

## License

This project is licensed under the MIT License.
