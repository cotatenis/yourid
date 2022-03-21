
BOT_NAME = 'yourid'
VERSION = "0-5-0"
SPIDER_MODULES = ['yourid.spiders']
NEWSPIDER_MODULE = 'yourid.spiders'

ROBOTSTXT_OBEY = False

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
MAGIC_FIELDS = {
    "timestamp": "$isotime",
    "spider": "$spider:name",
    "url": "$response:url",
}
SPIDER_MIDDLEWARES = {
    "scrapy_magicfields.MagicFieldsMiddleware": 100,
}

SPIDERMON_ENABLED = True
EXTENSIONS = {
    'yourid.extensions.SentryLogging' : -1,
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}
ITEM_PIPELINES = {
    "yourid.pipelines.DiscordMessenger" : 100,
    "yourid.pipelines.YourIdImagePipeline" : 200,
    "yourid.pipelines.GCSPipeline": 300,
    "spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 400,
}
SPIDERMON_VALIDATION_MODELS = (
    'yourid.validators.YouridItem',
)

SPIDERMON_SPIDER_CLOSE_MONITORS = (
'yourid.monitors.SpiderCloseMonitorSuite',
)

SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = True

SPIDERMON_MIN_ITEMS = 60
SPIDERMON_SENTRY_DSN = ""
SPIDERMON_SENTRY_PROJECT_NAME = ""
SPIDERMON_SENTRY_ENVIRONMENT_TYPE = ""
#THROTTLE
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 10
AUTOTHROTTLE_MAX_DELAY = 15
#GCP
GCS_PROJECT_ID = ""
GCP_CREDENTIALS = ""
GCP_STORAGE = ""
GCP_STORAGE_CRAWLER_STATS = ""
#FOR IMAGE UPLOAD
IMAGES_STORE = f''
IMAGES_THUMBS = {
    '400_400': (400, 400),
}

#DISCORD
DISCORD_WEBHOOK_URL = ""
DISCORD_THUMBNAIL_URL = ""
SPIDERMON_DISCORD_WEBHOOK_URL = ""

#LOG LEVEL
LOG_LEVEL='INFO'
