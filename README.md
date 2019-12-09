# Official Site

## Requirements

- pipenv

## Setup

```bash
1. `git clone https://github.com/mosquitone/official-site.git && cd official-site`
2. `pipenv install && pipenv shell`
3. `python ./manage.py migrate`
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
python ./manage.py loaddata ./official/fixtures/lateset.json
```

### setup aws cli

- When using 'aws configure' command.

  ```bash
  aws configure
  ```

- When not to use,and how to set environment variables.
  ```bash
  cli
  ```


  ### download media 

- 手動で aws コマンドを使用する場合を説明(for windows user とでも書いておく)
  ```bash
  aws s3 sync "s3://${AWS_BUCKET_NAME}" ./media/images 
  aws s3 sync "s3://${AWS_BUCKET_NAME}/original_images" ./media/original_images
  ```

- When using 'bin/download_images' file.
  ```bash
  env $(cat .env | xargs) ./bin/download_image
  ```

## Release site to production

To publish site from staging to production, first, install and setup Heroku CLI. after that, run following commands.

```bash
heroku run --app mosquitone ./bin/publish
```
