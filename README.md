# 📸 Django Photo Album Backend

A robust RESTful API backend for a modern photo album application, built with Django and Django REST Framework.

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="Django REST">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" alt="JWT">
</p>

---

## 🌟 Key Features

### 📷 Photo Management
- Upload high-resolution images with automatic thumbnails
- Organize photos into albums and categories
- EXIF data extraction (date, camera, location)

### 🔐 Secure Authentication
- JWT token authentication
- OAuth2.0 integration (Google, Facebook)
- Role-based permissions (Admin, User, Guest)

### ⚡ Performance Optimized
- Redis caching for frequent queries
- Background tasks for image processing
- Optimized database queries

---

## 🛠️ Tech Stack

| Component        | Technology                |
|------------------|---------------------------|
| **Framework**    | Django 4.2                |
| **API**          | Django REST Framework 3.14 |
| **Database**     | PostgreSQL 15             |
| **Authentication**| JWT + OAuth2              |


---

## 🚀 Installation Guide

### Prerequisites
- Python 3.10+
- PostgreSQL
- Redis

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/django_photo_album_backend.git
cd django_photo_album_backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your settings

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Development server
python manage.py runserver

# Production setup (using Gunicorn)
gunicorn config.wsgi:application --bind 0.0.0.0:8000
