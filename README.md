# Poultry Farming Management System

## Overview

The Poultry Farming Management System is designed to streamline the operations of a poultry farm. This system allows farm owners to manage vendors, track egg batches, monitor inventory, handle customer orders, manage rewards, and track sales through a centralized, user-friendly interface. The backend is built using Django and Django REST Framework, providing robust and scalable solutions for data management and API interactions.

## Project Structure

### Directories and Files

- **poultry_farm/**: This is the main project directory that contains the global settings and configurations.
  - **settings.py**: Contains all the settings and configuration for the Django project, including installed apps, middleware, database configuration, and more.
  - **urls.py**: The URL configuration file for the entire project. It routes URLs to appropriate view functions or classes.
  - **wsgi.py**: The entry point for WSGI-compatible web servers to serve the Django project.

- **farm/**: This directory contains the core application logic for the poultry farming system.
  - **models.py**: Defines the database models for Vendors, Batches, Inventory, Customers, Orders, Rewards, and Sales. These models represent the core data structures used throughout the system.
  - **serializers.py**: Contains the serializers for each model, converting model instances to JSON format and vice versa, facilitating smooth API interactions.
  - **views.py**: Implements viewsets for each model, defining the CRUD operations and business logic for interacting with the data.
  - **admin.py**: Registers models with the Django admin site, enabling easy management of data through the admin interface.
  - **urls.py**: Defines URL patterns for the farm application, linking URLs to the appropriate viewsets.
  - **tests.py**: Contains test cases to ensure the integrity and functionality of the application.

- **manage.py**: A command-line utility that lets you interact with the Django project in various ways, such as running the development server, creating migrations, and managing the database.

## Functionality

### Vendor Management

- **Create Vendor**: Add new vendors providing eggs for the farm.
- **Read Vendor**: View a list of all vendors and their details.
- **Update Vendor**: Modify vendor information.
- **Delete Vendor**: Remove a vendor from the system.

### Batch Management

- **Create Batch**: Record new batches of eggs received from vendors.
- **Read Batch**: View details of all egg batches, including vendor information and hatch rates.
- **Update Batch**: Update batch details as necessary.
- **Delete Batch**: Remove a batch from the system.

### Inventory Management

- **Create Inventory Record**: Add new inventory records for chicks.
- **Read Inventory**: View the current inventory status, including day-old, week-old, and 21-day-old chicks.
- **Update Inventory**: Modify inventory details as needed.
- **Delete Inventory**: Remove inventory records from the system.

### Customer and Order Management

- **Create Customer**: Add new customers to the system.
- **Read Customer**: View customer details and order history.
- **Update Customer**: Update customer information.
- **Delete Customer**: Remove a customer from the system.

- **Create Order**: Record new orders placed by customers.
- **Read Order**: View all orders, including customer details and order items.
- **Update Order**: Modify order details if necessary.
- **Delete Order**: Cancel or remove an order from the system.

### Reward Management

- **Create Reward**: Define new reward rules for customers.
- **Read Reward**: View all rewards and their criteria.
- **Update Reward**: Modify reward criteria as needed.
- **Delete Reward**: Remove a reward rule from the system.

### Sales Management

- **Create Sale**: Record sales transactions.
- **Read Sale**: View all sales, including customer and inventory details.
- **Update Sale**: Modify sale details if necessary.
- **Delete Sale**: Remove a sale record from the system.

## Design Choices

### Django and Django REST Framework

Django was chosen for its robustness, scalability, and ease of use. It provides a solid foundation for rapid development and maintenance. Django REST Framework (DRF) was selected for its powerful features and flexibility in building web APIs, making it ideal for creating the RESTful endpoints required for this project.

### Model-View-Controller (MVC) Pattern

The project follows the MVC pattern, separating the concerns of data (Models), user interface (Views), and control logic (Controllers). This separation ensures a clean and maintainable codebase, making it easier to extend and modify the system as needed.

### Token-Based Authentication

DRF's token-based authentication was implemented to secure the API endpoints. This approach ensures that only authenticated users can access or modify the data, enhancing the security of the system.

### Input Validation and Security

All input data is validated using Django's built-in validators and DRF's serializer validation. This ensures that only valid data is accepted, preventing common security issues such as SQL injection and cross-site scripting (XSS).

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/donshammah96/poultry_farm_management.git
   cd poultry_farm_management
   ```

2. **Create and activate a virtual environment**:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Run migrations**:

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser**:

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```sh
   python manage.py runserver
   ```

### Accessing the System

- **API Endpoints**: `http://localhost:8000/api/`
- **Admin Interface**: `http://localhost:8000/admin/`

## Conclusion

The Poultry Farming Management System is a comprehensive solution designed to streamline the operations of a poultry farm. With features for managing vendors, batches, inventory, customers, orders, rewards, and sales, it provides a centralized platform for efficient farm management. Built with Django and Django REST Framework, it ensures scalability, security, and ease of use. We hope this system meets your needs and enhances your farm's productivity.

