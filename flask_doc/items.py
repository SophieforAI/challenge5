# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FlaskDocItem(scrapy.Item):
    # define the fields for your item here like:
    item_url = scrapy.Field()
    item_text = scrapy.Field()




