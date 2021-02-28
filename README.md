# ngru
Recruitment task  
To properly run the project poetry is highly recommended. Instructions
on how to do it are available at the bottom of README.


### Example .env 

    DJANGO_KEY=nb-=b1lif_low2c#w&!ly9($u68k$oamnv7u2mpu5!0%tmv+5)
    DEBUG=False
    DB_NAME=cars
    DB_TEST_NAME=cars_test
    DB_USER=ngru
    DB_PASSWORD=ngru_postgres
    DB_PORT=5430
    DB_HOST=127.0.0.1
    
## Update tables in a database

`python manage.py migrate`

## Run development server

`python manage.py runserver`

## Build and run dockerized server

`docker-compose up --build`

## Running tests

Run `pytest .`. The results will be listed in the terminal.  

# Developer Checklist

## Database

Any models to makemigrations?  
Any unapplied migrations?


## Django tests

`python manage.py test`

## Code quality

`flake8` - check stylistics  
`black .` - reformat all  
`isort .` - sort import accordingly to the project's rules

# OpenAPI

Available at /swagger/

# Poetry

[Install the tool](https://python-poetry.org/docs/#installation)  
[Install the dependencies](https://python-poetry.org/docs/cli/#install)  
[Set env](https://python-poetry.org/docs/managing-environments/#switching-between-environments)  
[Run inside env](https://python-poetry.org/docs/cli/#run)  
[Build](https://python-poetry.org/docs/cli/#build)  
[Update](https://python-poetry.org/docs/cli/#update)
