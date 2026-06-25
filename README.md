# Multi Vendor Inventory System

## Overview

A FastAPI-based backend application that manages inventory items, vendors, and purchase orders.

The system supports:

* Centralized stock management
* Vendor management
* Many-to-many relationship between Items and Vendors
* Purchase Order creation
* Vendor validation before order creation

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite (Development)
* PostgreSQL Ready
* Pytest

---

## Architecture

Layered Architecture:

API Layer
↓
Service Layer
↓
Repository Layer
↓
Database Layer

Design Principles:

* SOLID Principles
* Repository Pattern
* Dependency Injection
* Separation of Concerns

---

## Features

### Stock Management

* Create Item
* Get Items

### Vendor Management

* Create Vendor
* Get Vendors

### Item Vendor Association

* Link Vendors to Items

### Purchase Orders

* Create Purchase Orders
* Validate Vendor Mapping

---

## API Endpoints

### Items

POST /items

GET /items

### Vendors

POST /vendors

GET /vendors

### Item Vendor Mapping

POST /item-vendor/link

### Purchase Orders

POST /orders

---
The application uses SQLAlchemy ORM and is database agnostic.

For development, SQLite is used.

To use PostgreSQL, update DATABASE_URL in .env and ensure PostgreSQL is installed and running.
## Running Application

Create Virtual Environment

python -m venv .venv

Activate Environment

Windows:

.venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Application

uvicorn app.main:app --reload

Swagger UI

http://localhost:8000/docs

---

## Running Tests

pytest

---

## Author

Nilesh Dokhe
