# -*- coding: utf-8 -*-
import os
LOGPATH = '../log/toutiao/'
DATAPATH = '../data/toutiao/'
CATEGORY = {
        '__all__':0,                  #推荐
        'news_hot':1,                 #热点
        'video':2,                    #视频
        'news_society':3,             #社会
        'news_entertainment':4,       #娱乐
        'news_tech':5,                #科技
        'news_sports':6,              #体育
        'news_car':7,                 #汽车
        'news_finance':8,             #财经
        'funny':9,                    #搞笑
        'news_military':10,            #军事
        'news_fashion':11,             #时尚
        'news_travel':12,              #旅游
        'news_food':13,                #美食
        'news_baby':14,                #育儿
        }
for (cname,cid) in CATEGORY.items():
    cmd ='scrapy crawl toutiao --logfile=%s%s.log -o %s%s.json -t json -a category=%s' % (LOGPATH,cname,DATAPATH,cname,cname)
    os.system(cmd)
    print 'cmd, ',cmd
