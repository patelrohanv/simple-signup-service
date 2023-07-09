# My Django Application

This is a simple Django application serving a signup page.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Steps

### 1. Create a Virtual Environment

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python virtual environments for them.

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

On macOS and Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
.\venv\Scripts\activate
```

You’ll know your virtual environment is activated because your shell prompt will change to show the name of the activated environment.

## Installing Dependencies

Once the virtual environment is activated, you can install the dependencies that your project needs. If you have a `requirements.txt` file, you can install all necessary dependencies by running:

```bash
pip install -r requirements.txt
```

This command installs the packages specified in the requirements.txt file. Make sure to run this command while your virtual environment is activated.

## Using My Django Application

After setting up the virtual environment and installing the necessary dependencies, you can start using the Django application.

1. **Migrate the Database**

    Django uses a database to store data. Before you can use the application, you need to create the necessary database tables. Django comes with a built-in migration system that automatically manages your database schema. To create the tables in your database, run:

    ```bash
    python manage.py migrate
    ```

2. **Run the Server**

    You can start the Django development server to see your application in action. Run the following command:

    ```bash
    python manage.py runserver
    ```

    This will start the server at `localhost:8000` by default. You can access your application by opening your web browser and navigating to `http://localhost:8000`.

3. **Create a Superuser (Optional)**

    If your application has an admin panel (which is created by default in Django projects), you might want to create a superuser account to access it. Run the following command and provide the necessary details:

    ```bash
    python manage.py createsuperuser
    ```

    After creating the superuser, you can access the admin panel at `http://localhost:8000/admin`.

4. Register Users on the Form

To register a new user, navigate to the user registration form at `http://localhost:8000/userapp/create`. Fill out the form with the user's details and submit it.

5. See Registered Users

To see the list of registered users, navigate to `http://localhost:8000/userapp/list`. This page will display a list of all users who have registered through the form.

## Running Tests

## Deployment
