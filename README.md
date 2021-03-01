# ngru
Recruitment task  
To properly run the project poetry is highly recommended. Instructions
on how to do it are available at the bottom of README.

## Used packages
requests - connection to external api  
djangorestframework - used to provide basic behaviour to all REST stuff  
flake8 - code formatting
isort - autoformatting imports
black - reformatting code (fixing line breaks, quotes)
gunicorn - used to reduce strain on server  
pytest - used for writing test  
psycopg2 - used because of postgres db being used by app  
python-decouple - separation of sensitive info, easier split between dev and prod env


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

Run `pytest .`. The results will be listed in the terminal.  
To run only a category of tests append: `-m` and specify which tests to run.

- unit
- integration

You can combine the categories with `or` keyword ex. `pytest -m "unit or integration" .`

## Code quality

`flake8` - check stylistics  
`black .` - reformat all  
`isort .` - sort import accordingly to the project's rules

# Poetry

[Install the tool](https://python-poetry.org/docs/#installation)  
[Install the dependencies](https://python-poetry.org/docs/cli/#install)  
[Set env](https://python-poetry.org/docs/managing-environments/#switching-between-environments)  
[Run inside env](https://python-poetry.org/docs/cli/#run)  
[Build](https://python-poetry.org/docs/cli/#build)  
[Update](https://python-poetry.org/docs/cli/#update)
