import os
LOGPATH = '../log/weibotv/'
DATAPATH = '../data/weibotv/'
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
