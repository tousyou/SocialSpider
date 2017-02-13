# -*- coding: utf-8 -*-
import json

if __name__ == '__main__':
    fd = open('../../data/anyv/amuse.json','rw+')
    line = fd.read()
    #print 'file, ',line
    weixinhao = json.loads(line,encoding='utf-8')
    for item in weixinhao:
        print 'pid,',item['pid']
        #print 'nickname,',item['nickname'].encode('utf-8')
        print 'nickname,',item['nickname']
    pass
