# Official Site

## Requirements

- pipenv
- heroku cli

## Setup

```bash
git clone https://github.com/mosquitone/official-site.git && cd official-site
pipenv install && pipenv shell
python ./manage.py migrate
```

## Start app

```bash
python ./manage.py runserver
```

## Release 

publish staging to production

```bash
heroku login
heroku run --app mosquitone ./publish.sh
```

## Initial Data

```bash
python ./manage.py loaddata ./official/fixtures/latest.json
env $(cat .env | xargs) ./download_image.sh
```