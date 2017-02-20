# -*- coding: utf-8 -*-
import os
WKDIR = '/root/dev/SocialSpider'
LOGPATH = WKDIR + '/log/anyv/'
DATAPATH = WKDIR + '/data/anyv/'
os.system('mkdir -p %s' % LOGPATH)
os.system('mkdir -p %s' % DATAPATH)
CATEGORY = {'news':2,               #新闻
            'economics':51,         #财经
            'technology':19,        #科技
            'read':25,              #阅读
            'funny':3,              #搞笑
            'amuse':20,             #趣玩
            'fashion':22,           #时尚
            'live':23,              #生活
            'health':26,            #健康
            'tour':27,              #旅游
            'sport':28,             #运动
            'video':29,             #影音
            'education':21,         #教育
            'brand':70,             #品牌
            'shopping':80,          #购物
            'star':1,               #明星
            'famous':18,            #名人
            'beauty':24,            #美女
            }
for (cname,cid) in CATEGORY.items():
    cmd ='scrapy crawl anyvspider --logfile=%s%s.log -a category=%s -s BLOOM_FILE=%s%s.bl -s JSON_FILE=%s%s.json' % (LOGPATH,cname,cid,DATAPATH,cname,DATAPATH,cname)
    os.system(cmd)
    print 'cmd, ',cmd
