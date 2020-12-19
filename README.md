# Food App using Django

## Setting up the environment

```python
    # Python version - 3.7.7
    # Create a venv
    python -m venv venv
    # Activate the venv (Windows)
    venv/Scripts/activate
    # Activate the venv (Linux and MacOs)
    source venv/bin/activate
    # Install the requirements
    pip install -r requirements.txt
```

## Starting the Django Project

```python
    # Start project
    django-admin startproject mysite
```

## Creating the food app

```python
    cd mysite
    python manage.py startapp food
```

## Add it to the installed apps

```python
    INSTALLED_APPS = [
        'food.apps.FoodConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
```

## Run initial migrations for the data model

```python
    python mange.py makemigrations food

    # food/migrations/0001_initial.py file includes code to create Food data model
```

## Apply generated migrations

```python
    python manage.py migrate food
```

## Run Server

```python
    python manage.py runserver
```
