import scrapy
import pymongo
from ..items import QuoteItem, AuthorItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    custom_settings = {
    'FEEDS': {
        'output/quotes.json': {
            'format': 'json',
            'encoding': 'utf8',
            'store_empty': False,
            'fields': None,
            'indent': 4,
            'item_export_kwargs': {
                'export_empty_fields': True,
            },
        },
    },
}
    
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css(".quote"):
            # print(quote)
            quote_item = QuoteItem()
            quote_item["text"] = quote.css("span.text::text").get()
            quote_item["author"] = quote.css("span small::text").get()
            quote_item["tags"] = quote.css("a.tag::text").get()
            # print(quote_item)
            yield quote_item
            
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
            
class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    custom_settings = {
    'FEEDS': {
        'output/authors.json': {
            'format': 'json',
            'encoding': 'utf8',
            'store_empty': False,
            'fields': None,
            'indent': 4,
            'item_export_kwargs': {
                'export_empty_fields': True,
            },
        },
    },
}
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        authors_urls = response.css('.author + a::attr(href)').extract()
        for author_url in authors_urls:
            yield response.follow(author_url, self.parse_authors)
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
            
    def parse_authors(self, response):
        author_item = AuthorItem()
        author_item['fullname'] = response.css("h3.author-title::text").get().strip()
        author_item['born'] = response.css("span.author-born-date::text").get().strip()
        author_item['bio'] = response.css("div.author-description::text").get().strip()
        yield author_item