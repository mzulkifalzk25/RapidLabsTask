
# RapidLabsTask - Django REST API with Celery

This project is a Django REST API with Celery for background task management. The project includes CRUD operations, user role management, JWT-based authentication, and scheduled tasks using Celery.

## Requirements

- Python 3.x
- Django 5.1.1
- Celery 5.4.0
- Redis (as the message broker for Celery)
- Other dependencies listed in `requirements.txt`

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/mzulkifalzk25/RapidLabsTask.git
cd RapidLabsTask
```

### Step 2: Set Up a Virtual Environment

Create a virtual environment to install dependencies in an isolated environment.

```bash
python -m venv .env
source .env/bin/activate  # For Linux/Mac
.env\Scripts\activate     # For Windows
```

### Step 3: Install Dependencies

Install all dependencies from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Step 4: Configure Redis (if not already installed)

Install and start Redis as it is used as a message broker for Celery.

- **For Windows**: You may need to download Redis from [here](https://github.com/microsoftarchive/redis/releases).
- **For Linux/Mac**: Run the following command to start Redis:
  
  ```bash
  sudo service redis-server start
  ```

### Step 5: Set Up Django Project

1. **Apply Migrations**:

    ```bash
    python manage.py migrate
    ```

2. **Create a Superuser** (for accessing the Django admin panel):

    ```bash
    python manage.py createsuperuser
    ```

3. **Run the Django Server**:

    ```bash
    python manage.py runserver
    ```

### Step 6: Start Celery Worker

Run the Celery worker to handle asynchronous tasks.

```bash
celery -A RapidLabsTask worker --loglevel=info
```

### Step 7: Start Celery Beat (for Scheduled Tasks)

Run Celery Beat to enable periodic task scheduling.

```bash
celery -A RapidLabsTask beat --loglevel=info
```

### Step 8: Test the API in Postman

1. **Authentication**: Obtain a JWT token by logging in through the `/api/token/` endpoint.
2. **CRUD Operations**: Test CRUD operations for your models.
3. **Scheduled Tasks**: Verify that scheduled tasks run every 10 seconds by monitoring the Celery logs.

## API Endpoints

| Endpoint                | Method | Description                    |
|-------------------------|--------|--------------------------------|
| `/api/token/`           | POST   | Obtain JWT token               |
| `/api/tasks/`           | GET    | List all tasks                 |
| `/api/tasks/<id>/`      | GET    | Retrieve a specific task       |
| `/api/tasks/`           | POST   | Create a new task              |
| `/api/tasks/<id>/`      | PUT    | Update an existing task        |
| `/api/tasks/<id>/`      | DELETE | Delete a specific task         |

### Testing Tasks

To verify the scheduled tasks:
- Ensure Celery and Celery Beat are running.
- Observe the Celery Beat log; you should see a scheduled task run every 24 hours at reset 00:00.

## Additional Notes

- Make sure Redis is running in the background for Celery to function.
- If you face issues with Redis, check the connection settings in `settings.py`.

