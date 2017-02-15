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
    cmd ='scrapy crawl weibotv --logfile=%s%s.log -o %s%s.json -t json -a category=%s' % (LOGPATH,cname,DATAPATH,cname,cname)
    os.system(cmd)
    print 'cmd, ',cmd
