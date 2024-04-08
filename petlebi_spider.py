## Serkan Ertaş
## Middle East Technical University NCC
import scrapy


class ProductSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://www.petlebi.com/"]

    def parse(self, response):
        selector1 = "ul[class='mobile-sub wsmenu-list']"
        selector2 = "li[class='wsshoplink-active'] div[class='wstitemright clearfix wstitemrightactive'] div[class='col-lg-12 col-md-12 clearfix'] ul li"
        categoryList = response.css(selector1)[0].css(selector2)

        for category in categoryList:
            yield scrapy.Request(
                url=category.css("li a::attr(href)").extract_first(),
                callback=self.parse_category_to_product,
            )

    def parse_category_to_product(self, response):
        product_links = response.css("#products a::attr(href)").extract()

        for eachlink in product_links:
            yield scrapy.Request(url=eachlink, callback=self.parse_main_item)

        next_page = response.css("link[rel='next']::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_category_to_product)

    def parse_main_item(self, response):

        jsDict = eval(
            response.css("script[type = 'application/ld+json']::text")
            .extract_first()
            .replace("\n", "")
            .replace("\r", "")
            .replace("\t", "")
        )

        url = jsDict["offers"]["url"]
        category = jsDict["category"]
        brand = jsDict["brand"]["name"]
        name = jsDict["name"]
        price = float(jsDict["offers"]["price"])
        priceCurrency = jsDict["offers"]["priceCurrency"]
        images = response.css(
            "div[class = 'row product-detail-main'] img::attr(src)"
        ).extract()

        sku = jsDict["sku"]
        if not sku:
            sku = ""

        yield {
            "url": url,
            "category": category,
            "brand": brand,
            "name": name,
            "price": price,
            "priceCurrency": priceCurrency,
            "images": images,
            "sku": sku,
        }
