import scrapy


class YelpCrawlSpider(scrapy.Spider):
    name = "yelp_crawl"
    allowed_domains = ["www.yelp.com"]
    start_urls = ["https://www.yelp.com/search?find_desc=Restaurants&find_loc=San Francisco, CA&ns=1"]

    def parse(self, response):
        businesses = response.xpath("//li[contains(@class,'css')]/div[contains(@class,'container')]/div[contains(@class,'css')]")
        for i in businesses:
            print(i)