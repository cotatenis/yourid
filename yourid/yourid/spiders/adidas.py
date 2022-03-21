from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from yourid.items import YouridItem
from scrapy.loader import ItemLoader
from scrapy.utils.project import get_project_settings
from w3lib.html import remove_tags, strip_html5_whitespace

class YourIdAdidasSpider(CrawlSpider):
    settings = get_project_settings()
    version = settings.get("VERSION")
    name = 'yourid-adidas'
    allowed_domains = ['youridstore.com.br']
    start_urls = ['https://youridstore.com.br/tenis/tenis-adidas.html/']
    product_details = LinkExtractor(restrict_xpaths="//div[@class='product-image-wrapper']")
    pagination = LinkExtractor(restrict_xpaths=("//div[@class='pager']//ol//a"))
    rules = [Rule(product_details, callback='parse_products'), Rule(pagination, follow=True)]

    def parse_products(self, response):
        if response.url not in self.start_urls:
            product_container = response.xpath("//div[@class='product-view container']")
            sizes = [d.replace("\n","").strip() for d in response.xpath("//span[@class='swatch-label']/text()").getall() if d.replace("\n","").strip().isdigit()]
            images = response.xpath("//img[@class='lazyOwl']/@data-src").getall()
            i = ItemLoader(item=YouridItem(), selector=product_container)
            i.add_xpath("product", "//div[@class='product-name']/h1")
            i.add_value("url", response.url)
            i.add_xpath("description", "//div[@class='box-collateral box-description']/div")
            i.add_xpath("price", "//span[@class='price']")
            i.add_xpath("currency", "//span[@class='price']")
            i.add_xpath("genre", "//span[@class='gen']")
            i.add_xpath("sku", "//div[@class='sku']/span[@class='value']")
            i.add_value("image_urls", self.parse_images_urls(images))
            i.add_value("image_uris", self.parse_images_uri(response, images=images))
            i.add_xpath("brand", "//div[@class='brand']/h2")
            i.add_value("sizes", sizes)
            i.add_value("spider_version", self.version)
            i.add_value("spider", self.name)
            yield i.load_item()
    
    @staticmethod
    def parse_images_urls(images):
        url_container = []
        for image in images:
            hash_image = image.split("/")[-4]
            num_cache = image.split("/")[-7]
            filename = image.split("/")[-1]
            letter_folder_1 = image.split("/")[-3] 
            letter_folder_2 = image.split("/")[-2] 
            url_container.append(
                f"https://youridstore.com.br/media/catalog/product/cache/{num_cache}/image/1200x/{hash_image}/{letter_folder_1}/{letter_folder_2}/{filename}"
            )
        return url_container
    
    def parse_images_uri(self, response, images):
        sku = strip_html5_whitespace(remove_tags(response.xpath("//div[@class='sku']/span[@class='value']").get()))
        image_uris = [f"{self.settings.get('IMAGES_STORE')}{sku}_{filename.split('/')[-1]}" for filename in images]
        return image_uris

