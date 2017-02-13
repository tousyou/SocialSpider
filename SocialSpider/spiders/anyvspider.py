# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.selector import HtmlXPathSelector
from SocialSpider.items import CnblogsItem
from scrapy.http import Request
from SocialSpider.items import WxhaoItem

class AnyvSpider(scrapy.Spider):
    name = "anyvspider"
    allowed_domains = ["anyv.net"]
    start_urls = (
        'http://www.anyv.net/',
    )

    def __init__(self,category=None,*args,**kwargs):
        super(AnyvSpider,self).__init__(*args,**kwargs)
        self.start_urls = [
                'http://www.anyv.net/index.php/category-%s' % category,]
    def parse(self, response):
        self.log("Fetch anyv homepae :%s" % response.url)
        hxs = HtmlXPathSelector(response)

        items = hxs.select('//div[@class="newpicsmall_list"]/a')
        a_page = hxs.select('//div/a[@class="next"]')

        for weixin in items:
            item = WxhaoItem()
            in_url = (weixin.select('@href').extract())[0]
            if len(in_url) > 0:
                #print 'in_url, ', in_url
                time.sleep(0.1)
                yield scrapy.Request(in_url,callback=self.parseWxhao, meta={'item': item})
        
        url = (a_page.select('@href').extract())[0]
        if len(url) > 0:
            time.sleep(1)
            yield scrapy.Request(url,callback=self.parse)
        pass

    def parseWxhao(self, response):
        item = response.meta['item']
        hxs = HtmlXPathSelector(response)
        a_page = hxs.select('//div[@id="article_extinfo"]')
        item['nickname'] = (a_page.select('//h1').select('text()').extract())[0]
        txt = (a_page.select('//h5').select('text()').extract())[0].split(':',-1)
        item['pid']=txt[1]
        
        yield item

