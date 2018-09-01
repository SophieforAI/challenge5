# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule

from scrapy.linkextractors import LinkExtractor
from flask_doc.items import FlaskDocItem




class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    #allowed_domains = ['flask.pocoo.org/docs/0.12/']
    start_urls = ['http://flask.pocoo.org/docs/0.12']
    rules= (
        Rule(LinkExtractor(allow='flask.pocoo.org/docs/0.12/.*'),callback='parse_Scorpion',follow=True),
        )

    def parse_Scorpion(self, response):
        yield FlaskDocItem({
            'url': response.url,
            'text': ''.join(response.css('::text').extract())
        })
'''
    def parse_parse(self, response):
        item = FlaskDocItem()
        for url in response.css(li.toctree-l1):
            item['item_url'] = response.urljoin(url.css('a::attr(href)').extract_first()) 
        
            for url_u in url.css('li.toctree-l2'):
                item['item_url'] = response.urljoin(url_u.css('a::attr(href)').extract_first())
        
                request = scrapy.Request(item['item_url'], callback=self.parse_text)    
                request.meta['item'] = item
                yield request
    def parse_text(self,response):
        item = response.meta['item']
        item['text'] = response.css('::text').extract()
        print(item)
        yield item 


'''
