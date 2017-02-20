# -*- coding: utf-8 -*-
import time
import scrapy
import re
import bs4
from scrapy.selector import HtmlXPathSelector
from SocialSpider.items import WbtvItem
from scrapy.http import Request

class WeibotvSpider(scrapy.Spider):
    name = "weibotv"
    allowed_domains = ["weibo.com"]
    #start_urls = (
    #    'http://www.weibo.com/tv/vfun/',
    #)
    #next_urls = 'http://www.weibo.com/p/aj/v6/mblog/videolist?type=vfun&page=%d&end_id=%s&__rnd=%d'
    
    def __init__(self, category=None, *args, **kwargs):
        super(WeibotvSpider,self).__init__(*args,**kwargs)
        self.start_urls = ['http://www.weibo.com/tv/%s/' % category]
        self.next_urls = 'http://www.weibo.com/p/aj/v6/mblog/videolist?type=%s' % category
    def parse(self,response):
        self.log("Fetch weibotv homepage page: %s" % response.url)
        body = response.body.replace('\\"','"')
        #print 'resp, ',body
        soup = bs4.BeautifulSoup(body, "html.parser" )
        tags = soup.find_all("a")
        length = 0
        last_mid = ''
        for tag in tags:
            if 'mid' not in str(tag):
                continue
            last_mid = tag.get("mid")
            item = WbtvItem()
	    item['Type'] = 'mid'
            item['mid']=last_mid
            length = length + 1
            #print 'mid, ',last_mid
            yield item
        if length > 0:
            url = self.next_urls + '&page=%d&end_id=%s&__rnd=%d' % (1,last_mid,int( time.time() * 1000))  
            yield Request(url,callback=self.parse)
        pass

