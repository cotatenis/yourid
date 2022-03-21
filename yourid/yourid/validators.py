from schematics.models import Model
from schematics.types import URLType, StringType, ListType, FloatType, DateTimeType, BooleanType, ModelType

class YouridItem(Model):
    product = StringType(required=True)
    url = URLType(required=True)
    description = StringType()
    genre = StringType()
    sku = StringType(required=True)
    price = FloatType(required=True)
    currency = StringType()
    brand = StringType()
    sizes = ListType(StringType)
    image_uris = ListType(StringType, required=True)
    timestamp = DateTimeType(required=True)
    spider = StringType(required=True)
    spider_version = StringType(required=True)