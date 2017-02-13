# -*- coding: utf-8 -*-
import os
LOGPATH = '../log/anyv/'
DATAPATH = '../data/anyv/'
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
    cmd ='scrapy crawl anyvspider --logfile=%s%s.log -o %s%s.json -t json -a category=%s' % (LOGPATH,cname,DATAPATH,cname,cid)
    os.system(cmd)
    print 'cmd, ',cmd
