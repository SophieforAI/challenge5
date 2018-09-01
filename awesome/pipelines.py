# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import redis
import json

class AwesomePipeline(object):
    def process_item(self, item, spider):
        #item['text']=json.load(re.sub(r's',' ',item['text']))
       
        self.redis.lpush('awesome:items', json.dumps(dict(item)))
        return item

    def open_spider(self,spider):
        self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)
