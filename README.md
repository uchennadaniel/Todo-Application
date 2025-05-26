# Django Todo Application

A simple Todo web application built with Django.

## Features

- Add, update, and delete tasks
- Set task priority and due date
- Responsive Bootstrap UI

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the app**
6.  Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

```
todowebsite/
  todoapp/
    migrations/
    static/
      todoapp/
        style.css
    templates/
      html/
        base.html
        index.html
        delete.html
        Edit.html
    models.py
    views.py
    forms.py
  manage.py
```

## Notes

- To use the admin panel, create a superuser:
  ```bash
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

```
todowebsite/
  todoapp/
    migrations/
    static/
      todoapp/
        style.css
    templates/
      html/
        base.html
        index.html
        delete.html
        Edit.html
    models.py
    views.py
    forms.py
  manage.py
```

## Notes

- To use the admin panel, create a superuser:
  ```bash
