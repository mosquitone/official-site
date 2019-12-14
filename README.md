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

```bash
python ./manage.py loaddata ./official/fixtures/lateset.json
```

### 1.setup aws cli

- Setting environment variables.

  ```bash
  aws configure
  AWS Access Key ID[]: ${AWS_ACCESS_KEY_ID}
  AWS Secret Access Key []: ${AWS_SECRET_ACCESS_KEY}
  Default region name []: ${AWS_DEFAULT_REGION}
  Default output format []: "text"
  ```

### 2.download media

#### When using 'aws' command.(for windowsOS user)

  ```bash
  aws s3 sync "s3://${AWS_BUCKET_NAME}/images" ./media/images
  aws s3 sync "s3://${AWS_BUCKET_NAME}/original_images" ./media original_images
  ```

#### When using 'bin/download_image' file.(for macOS/LinuxOS user)

before download fixture images, you need to create .env and define following env vars.

- AWS_ACCESS_KEY_ID
- AWS_BUCKET_NAME
- AWS_DEFAULT_REGION
- AWS_SECRET_ACCESS_KEY

```bash
env $(cat .env | xargs) ./bin/download_image
```

## Release site to production

To publish site from staging to production, first, install and setup Heroku CLI. after that, run following commands.

```bash
heroku run --app mosquitone ./bin/publish
```
