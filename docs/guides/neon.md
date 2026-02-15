# Connect Zimna to Neon Postgres

This guide explains how to connect the project to Neon Postgres.

**Important:**
- Must be run inside the backend directory.
- Retrieve access connection parameters from Neon console.
- All package installations must occur within an active Python virtual environment.

---

## 🛠️ Instructions

### 1. Ensure a Virtual Environment is Active

Check for a virtual environment directory (venv) in the project root. If one does not exist, create it immediately by running
```bash
python3 -m venv venv
```

Activate it by running:
For macOS/Linux
```bash
source venv/bin/activate
```

For Windows
```bash
venv\Scripts\activate
```

---

### 2. Install Dependencies

Install the required Python packages into the virtual environment:

```bash
pip install "psycopg[binary]" python-dotenv
```

- **`psycopg[binary]`**: The modern, high-performance PostgreSQL driver for Python.
- **`python-dotenv`**: To load database credentials from a `.env` file.

---

### 3. Configure Environment Variables

1.  Check for the presence of a `.env` file at the root of the project. If it doesn't exist, create one.
2.  Add the following connection parameters to the `.env` file and replace the values with the credentials from Neon.

    ```dotenv title=".env"
    PGHOST='aws-xxx-pooler.neon.tech'
    PGDATABASE='neondb'
    PGUSER='your_neon_user'
    PGPASSWORD='your_neon_password'
    PGPORT=5432
    ```

---

### 4. Update Django Settings

Modify the project's main `settings.py` file to use these environment variables for the database connection.

1.  **Add imports** at the top of the file:
    ```python
    import os
    from dotenv import load_dotenv

    # Load environment variables
    load_dotenv()
    ```
3.  **Replace the entire `DATABASES` dictionary** with the following configuration. This setup reads credentials from the `.env` file and includes best practices for connecting to Neon.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.getenv('PGHOST'),
            'NAME': os.getenv('PGDATABASE'),
            'USER': os.getenv('PGUSER'),
            'PASSWORD': os.getenv('PGPASSWORD'),
            'PORT': os.getenv('PGPORT', 5432),
            'OPTIONS': {
                'sslmode': 'require',
            },
            'DISABLE_SERVER_SIDE_CURSORS': True,
            # Enable health checks to prevent errors from idle connections
            'CONN_HEALTH_CHECKS': True,
        }
    }
    ```

---



### 5. Next Steps

Once the file modifications are complete:

1.  Run the initial database migrations:
    ```bash
    python manage.py migrate
    ```
2.  Start the Django development server:
    ```bash
    python manage.py runserver
    ```

---

### 6. Test the Connection

To test the connection, use backend/templates/test.html view and visit `http://localhost:8000` in the browser, where you should see the PostgreSQL version from the Neon database.

---

## ❌ Do Not

- **Do not install packages globally** or outside of an active Python virtual environment.
- **Do not hardcode credentials** or sensitive information in `settings.py` or any other source code file.
- Do not output the contents of the `.env` file or the user's connection string in any response.
- Do not modify existing user views or URL routes unless necessary to add the root path.
