from yourid.spiders.adidas import YourIdAdidasSpider

class YourIdNikeSpider(YourIdAdidasSpider):
    start_urls = ["https://youridstore.com.br/tenis/tenis-nike.html"]
    name = 'yourid-nike'