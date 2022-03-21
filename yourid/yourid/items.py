import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags, replace_escape_chars, strip_html5_whitespace
from scrapy.item import Item
from price_parser import parse_price

def cleaning_description(text):
    return text.replace("\u00ae", " ").replace("\xa0", " ")

def fetch_price(price):
    return float(parse_price(price).amount)

def fetch_currency(price):
    return parse_price(price).currency

def fetch_brand(brand):
    brand = brand.split("\n")[0].strip()
    brand = brand.replace("Masculino", "").replace("Feminino","").replace("Unissex","")
    return brand

def parse_sku(sku):
    if len(sku) > 6:
        return sku.replace(" ", "-")
    else:
        return sku

class YouridItem(Item):
    product = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace), output_processor=TakeFirst())
    url = scrapy.Field(input_processor=MapCompose(strip_html5_whitespace), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, cleaning_description, strip_html5_whitespace), output_processor=TakeFirst())
    genre = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, cleaning_description, strip_html5_whitespace), output_processor=TakeFirst())
    sku = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, cleaning_description, strip_html5_whitespace, parse_sku), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, cleaning_description, strip_html5_whitespace, fetch_price), output_processor=TakeFirst())
    currency = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, cleaning_description, strip_html5_whitespace, fetch_currency), output_processor=TakeFirst())
    brand = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, cleaning_description, strip_html5_whitespace, fetch_brand), output_processor=TakeFirst())
    sizes = scrapy.Field()
    image_uris = scrapy.Field()
    image_urls = scrapy.Field()
    timestamp = scrapy.Field()
    spider = scrapy.Field(output_processor=TakeFirst())
    spider_version = scrapy.Field(output_processor=TakeFirst())