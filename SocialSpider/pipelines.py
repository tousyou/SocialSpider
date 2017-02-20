# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import os

from scrapy.exceptions import DropItem
import logging
from pybloom import ScalableBloomFilter
import json

logger = logging.getLogger('my_pipelines')

class BloomPipeline(object):
    def __init__(self, bloomfile, spider_name):
        self.bloomfile = bloomfile
	self.spider_name = spider_name

        # item crawled before
        logger.info("loading crawled items before...")
        
	if os.path.isfile(self.bloomfile): 
	    f = open(self.bloomfile,'r')
	    self.item_crawled = ScalableBloomFilter.fromfile(f)
	    f.close()
	else:
            self.item_crawled = ScalableBloomFilter(100000000,0.001,
               mode=ScalableBloomFilter.SMALL_SET_GROWTH)

	cnt = self.item_crawled.count
        logger.info("pipline read %d crawled items" % cnt)

    def __del__(self):
	f = open(self.bloomfile,'w')
	self.item_crawled.tofile(f)
        f.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            #mongo_uri=crawler.settings.get('MONGODB_ADDRESS'),
            bloomfile = crawler.settings.get('BLOOM_FILE'),
            #bloomfile = "/root/dev/SocialSpider/data/weibotv/bloomfile",
	    spider_name = crawler.spidercls.name
        )

    def process_item(self, item, spider):
        #if not item['md5']:
        #    md5 = hashlib.md5("%s%s%s"%(item['title'].encode('utf-8'),item['url'].encode('utf-8'))).hexdigest()
        #    item['md5'] = md5

        valid = True
        item_id = ''
	if self.spider_name == 'weibotv':
	    item_id = item['mid']
	elif self.spider_name == 'toutiao':
	    item_id = item['Url']
	    #item_id = hashlib.md5("%s"%(item['Url'].encode('utf-8'))).hexdigest()
	elif self.spider_name == 'anyvspider':
	    item_id = item['pid']
	else:
	    pass

	if self.item_crawled.add(item_id):
	    valid = False
	else:
	    valid = True

        if valid:
            logger.info("item: %s wrote to bloomfile %s" % ( item_id.encode('utf-8'),self.bloomfile))
            return item
        else:
            logger.info("item droped %s " % item_id.encode('utf-8'))

class JsonPipeline(object):
    def __init__(self, jsonfile, spider_name):
	self.jsonfile = jsonfile
	self.spider_name = spider_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            jsonfile = crawler.settings.get('JSON_FILE'),
            #jsonfile = "/root/dev/SocialSpider/data/weibotv/json",
	    spider_name = crawler.spidercls.name
        )

    def open_spider(self, spider):
        self.file = open(self.jsonfile, 'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if item is not None:
    	    line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        return item

