## Running by Docker

To run the development version of the app

```bash
docker compose up
```

Go to `http://localhost:5173` to see the web
Go to `http://localhost:9090` for database management (phpmyadmin)

Note: The list of `environment:` variables in the `docker compose.yml` file takes precedence over any variables specified in `.env`.

To run any commands using the `Flask CLI`

```bash
docker compose run --rm manage <<COMMAND>>
```

Therefore, to initialize a database and apply migration you would run

```bash
docker compose run --rm manage db init
docker compose run --rm manage db migrate
docker compose run --rm manage db upgrade
```

### Running locally

Run the following commands to bootstrap your environment if you are unable to run the application using Docker

```bash
cd backend
pip install -r requirements/dev.txt
```

#### Database Initialization (locally)

Once you have installed your DBMS, run the following to create your app
database tables and perform the initial migration

```bash
flask db init
flask db migrate
flask db upgrade
```

## Shell

To open the interactive shell, run

```bash
docker compose run --rm manage shell
flask shell # If running locally without Docker
```

By default, you will have access to the flask `app`.

## Running Tests/Linter

To run all tests, run

```bash
docker compose run --rm manage test
flask test # If running locally without Docker
```

To run the linter, run

```bash
docker compose run --rm manage lint
flask lint # If running locally without Docker
```

The `lint` command will attempt to fix any linting/style errors in the code. If you only want to know if the code will pass CI and do not wish for the linter to make changes, add the `--check` argument.

## Migrations

Whenever a database migration needs to be made. Run the following commands

```bash
docker compose run --rm manage db migrate
flask db migrate # If running locally without Docker
```

This will generate a new migration script. Then run

```bash
docker compose run --rm manage db upgrade
flask db upgrade # If running locally without Docker
```

To apply the migration.

For a full migration command reference, run `docker compose run --rm manage db --help`.

If you will deploy your application remotely (e.g on Heroku) you should add the `migrations` folder to version control.
You can do this after `flask db migrate` by running the following commands

```bash
git add migrations/*
git commit -m "Add migrations"
```


