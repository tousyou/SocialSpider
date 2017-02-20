# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import Request
from SocialSpider.items import UrlItem


class ToutiaoSpider(scrapy.Spider):
    name = "toutiao"
    allowed_domains = ["toutiao.com"]
    category = ''
    def __init__(self, category=None, *args, **kwargs):
        super(ToutiaoSpider,self).__init__(*args,**kwargs)
        #self.start_urls = ['http://www.toutiao.com/api/article/feed/?category=%s&utm_source=toutiao&widen=0&max_behot_time=0&max_behot_time_tmp=0&as=A135B8B16A0CF6F&cp=581AACBF560FEE1' % category]
        #self.next_urls = 'http://www.toutiao.com/api/article/feed/?category=%s&utm_source=toutiao&widen=0&max_behot_time=0' % category
        self.start_urls = ['http://www.toutiao.com/api/article/feed/?category=%s&utm_source=toutiao&widen=0&max_behot_time=0&max_behot_time_tmp=0&as=A105D8AA8AC798B&cp=58AAA7B9185B8E1' % category]
        self.next_urls = 'http://www.toutiao.com/api/article/feed/?category=%s&utm_source=toutiao&widen=0&max_behot_time=0' % category
        self.category = category

    def parse(self, response):
        self.log("Fetch toutiao homepage page: %s" % response.url)
        #print 'body, ',response.body
        rsp = json.loads(response.body)
        #print 'has_more, ', rsp['has_more']
        if rsp['has_more']:
            for val in rsp['data']:
		if 'ad' in val:
		    continue
                item = UrlItem()
                item['Type'] = 'url'
                item['Title'] = val['title'].encode('utf-8')
                item['Url'] = "http://www.toutiao.com" + val['source_url']
                item['Time'] = val['behot_time']
                item['Source'] = 'toutiao'
                #item['MediumUrl'] = val['media_url']
                item['Category'] = self.category
                if 'comments_count' in val:
                    item['HotValue'] = val['comments_count']
                print item['Title'],item['Url'],item['Time']
                yield item
            print 'max_behot_time, ', rsp['next']['max_behot_time']
            max_behot_time = rsp['next']['max_behot_time']
            
            url = self.next_urls + '&max_behot_time_tmp=%s&as=A105D8AA8AC798B&cp=58AAA7B9185B8E1' % max_behot_time  
            yield Request(url,callback=self.parse)

        pass
