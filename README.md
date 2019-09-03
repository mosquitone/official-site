# Official Site

## Requirements

- pipenv
- heroku cli

## Setup

```bash
git clone https://github.com/mosquitone/official-site.git && cd official-site
pipenv install && pipenv shell
python ./manage.py migrate
heroku login
```

## Start app

```bash
python ./manage.py runserver
```

## Release 

publish staging to production

```bash
heroku run --app mosquitone ./bin/publish
```

## Load Initial Data

before download images, you need to create .env and define following env vars.

- AWS_ACCESS_KEY_ID
- AWS_BUCKET_NAME
- AWS_DEFAULT_REGION
- AWS_SECRET_ACCESS_KEY

```bash
python ./manage.py loaddata ./official/fixtures/latest.json
env $(cat .env | xargs) ./bin/download_image
```
