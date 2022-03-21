
░█████╗░░█████╗░████████╗░█████╗░████████╗███████╗███╗░░██╗██╗░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝████╗░██║██║██╔════╝
██║░░╚═╝██║░░██║░░░██║░░░███████║░░░██║░░░█████╗░░██╔██╗██║██║╚█████╗░
██║░░██╗██║░░██║░░░██║░░░██╔══██║░░░██║░░░██╔══╝░░██║╚████║██║░╚═══██╗
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║░░░██║░░░███████╗██║░╚███║██║██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░


--------------------------------------------------------------------------

# Web crawler

url: [https://youridstore.com.br/](https://youridstore.com.br/)


# 1. Configuration
Before you run this project and for the proper running of this program you need to set up some variables inside `yourid/yourid/settings.py`.

## 1.1 SENTRY
This project utilizes [SENTRY](https://sentry.io/) for error tracking.

- `SPIDERMON_SENTRY_DSN`
- `SPIDERMON_SENTRY_PROJECT_NAME`
- `SPIDERMON_SENTRY_ENVIRONMENT_TYPE`

## 1.2 GOOGLE CLOUD PLATFORM

- `GCS_PROJECT_ID` 
- `GCP_CREDENTIALS`
- `GCP_STORAGE`
- `GCP_STORAGE_CRAWLER_STATS`
- `IMAGES_STORE`

## 1.3 DISCORD
- `DISCORD_WEBHOOK_URL`
- `DISCORD_THUMBNAIL_URL`
- `SPIDERMON_DISCORD_WEBHOOK_URL`

# 2. Build

```shell
cd maze
make docker-build-production
```

# 3. Publish

```shell
make docker-publish-production
```

# 4. Use

```shell
docker run gcr.io/cotatenis/cotatenis-crawl-yourid:0.5.0 --brand=adidas 
```
