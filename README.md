# Official Site

## Requirements

- pipenv

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

## Load Fixtures

before download fixture images, you need to create .env and define following env vars.

- AWS_ACCESS_KEY_ID
- AWS_BUCKET_NAME
- AWS_DEFAULT_REGION
- AWS_SECRET_ACCESS_KEY

```bash
[macOS]
python ./manage.py loaddata ./official/fixtures/latest.json
env $(cat .env | xargs) ./bin/download_image

[winOS]
python ./manage.py loaddata ./official/fixtures/2019-12-01.json
aws configure
aws s3 sync "s3://mosquitone-official-site/images" ./media/images && aws s3 sync "s3://mosquitone-official-site/original_images" ./media/original_images
```

## Release site to production

To publish site from staging to production, first, install and setup Heroku CLI. after that, run following commands.

```bash
heroku run --app mosquitone ./bin/publish
```
