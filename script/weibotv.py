# -*- coding: utf-8 -*-
import os
WKDIR = '/root/dev/SocialSpider'
LOGPATH = WKDIR + '/log/weibotv/'
DATAPATH = WKDIR + '/data/weibotv/'
os.system('mkdir -p %s' % LOGPATH)
os.system('mkdir -p %s' % DATAPATH)
CATEGORY = {
    'moe':0,            #萌宠萌娃   
    'vfun':1,           #搞笑
    'music':2,          #音乐
    'show':3,           #明星综艺
    }
for (cname,cid) in CATEGORY.items():
    cmd ='scrapy crawl weibotv --logfile=%s%s.log -a category=%s -s BLOOM_FILE=%s%s.bl -s JSON_FILE=%s%s.json' % (LOGPATH,cname,cname,DATAPATH,cname,DATAPATH,cname)
    os.system(cmd)
    print 'cmd, ',cmd
