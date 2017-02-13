# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from SocialSpider.items import CnblogsItem
from scrapy.http import Request
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = (
            'http://www.cnblogs.com/',
            )
    domains_url = 'http://www.cnblogs.com/'

    def parse(self, response):
        self.log("Fetch cnblogs homepage page: %s" % response.url)
        hxs = HtmlXPathSelector(response)
        #authors = hxs.select('//a[@class="titlelnk"]')

        items = hxs.select('//a[contains(@class,"titlelnk")]')
        a_page = hxs.select('//div[@class="pager"]/a')

        for author in items:
            #print author.select('text()').extract()
            item = CnblogsItem()
            #property
            item['Title'] = author.select('text()').extract()
            item['TitleUrl'] = author.select('@href').extract()
            yield item
        
        if len(a_page) > 0:
            for a_item in a_page:
                page_text = ''.join(a_item.xpath('text()').extract())
                if page_text == '下一页'.encode('utf-8') or 'Next' in page_text:
                    next_url = ''.join(a_item.xpath('@href').extract())
                    next_url = self.domains_url + next_url
                    print 'next_url, ',next_url
                    yield Request(next_url,callback=self.parse)
                    break
