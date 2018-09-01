# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from awesome.items import AwesomeItem


class AwesomeMovieSpider(scrapy.spiders.CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/subject/3011091/']
    rules = (
             Rule(LinkExtractor(allow='movie.douban.com/subject/.*/?from=subject-page'),callback='parse_movie_item',follow=True),
            )

    def parse_movie_item(self, response):
        yield AwesomeItem({
            'url':response.url,
            'name':response.css('h1::text'),
            'summary':response.xpath('//*[@id="link-report"]/span[1]/span/text()'),
            'score':response.css('strong::text')})
        return item

    def parse_start_url(self,response):
        yield self.parse_movie_item(response)

    def parse_page(self,response):
        yield self.parse_movie_item(response)

