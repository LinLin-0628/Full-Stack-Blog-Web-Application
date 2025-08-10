# Django Blog Platform

A full-featured blog web application built with Django, featuring user authentication, content management, and interactive commenting system.

## Features

### Core Functionality
- **User Authentication**: Registration, login/logout with email verification
- **Blog Management**: Create, read, and categorize blog posts
- **Commenting System**: Interactive commenting on blog posts
- **Search Functionality**: Search through blog titles and content
- **Email Verification**: SMTP-based captcha system for secure registration




## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/LinLin-0628/Full-Stack-Blog-Web-Application.git
cd Full-Stack-Blog-Web-Application
```

### 2. Set Up Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Configuration

1. Create a MySQL database with your preferred name (e.g., `blogplatform_db`)
2. Update database credentials in `BlogDemo/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 5. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser 
```bash
python manage.py createsuperuser
```

### 7. Run  Server
```bash
python manage.py runserver
```


