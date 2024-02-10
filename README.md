# Django API Project: Products CRUD with Categories and User Authentication

## Description

This Django API project implements CRUD operations for managing products and categories, along with user registration and authentication functionalities.

## Features

- **Products CRUD Operations:** Allows users to Create, Read, Update, and Delete products.
- **Categories Management:** Supports categorization of products for better organization.
- **User Registration:** Enables users to register with the system.
- **User Authentication:** Provides secure login functionality for registered users.

## Technologies Used

- **Django:** Python-based web framework used for backend development.
- **Django Rest Framework (DRF):** Powerful toolkit for building Web APIs in Django.
- **SQLite (or other preferred database):** Database management system for storing application data.

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd <project_directory>
```

3. Create a virtual environment and activate it:

```bash
virtualenv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate  # for Windows
```

4. Install dependencies:

```bash
pip install -r req.txt
```

5. Run database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

## API documentation:

```
http://localhost:8000/swagger/
```