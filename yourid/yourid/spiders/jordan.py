from yourid.spiders.adidas import YourIdAdidasSpider

class YourIdJordanSpider(YourIdAdidasSpider):
    start_urls = ["https://youridstore.com.br/tenis/tenis-jordan.html"]
    name = 'yourid-jordan'