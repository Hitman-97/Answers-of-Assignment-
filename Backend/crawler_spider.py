import scrapy
import json

class CrawlerSpider(scrapy.Spider):
    name = 'crawler_spider'
    allowed_domains = ['example.com']  # Modify for your target domain
    start_urls = ['http://example.com']  # Base URL for crawling

    def parse(self, response):
        page = {
            'url': response.url,
            'title': response.css('title::text').get(),
            'metadata': response.css('meta::attr(content)').getall(),
            'article_content': ' '.join(response.css('p::text').getall()),
            'links': response.css('a::attr(href)').getall()
        }

        # Saving extracted data
        with open('../../extracted_data.json', 'a') as f:
            f.write(json.dumps(page) + '\n')

        # Follow links for further crawling
        for link in page['links']:
            if link.startswith('http'):
                yield response.follow(link, self.parse)
