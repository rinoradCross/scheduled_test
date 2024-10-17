## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd scheduleproject
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## API Documentation

The project uses `drf-yasg` to generate Swagger documentation for the API. You can access the Swagger UI at:

http://localhost:8000/swagger/



## Authentication

The project uses JWT for authentication. You can obtain a token by making a POST request to:

http://localhost:8000/api/token/


Refresh the token by making a POST request to:

http://localhost:8000/api/token/refresh/


## Settings

The settings for the project are located in [`scheduleproject/settings.py`](scheduleproject/settings.py). Make sure to update the `SECRET_KEY` and other settings as needed.

## Static Files

Static files are served from the `staticfiles` directory. Make sure to collect static files before deploying to production:
```sh
`python manage.py collectstatic`


## License
This project is licensed under the BSD 3-Clause License. See the LICENSE file for more details.
