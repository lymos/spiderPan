# -*- coding: utf-8 -*-
import urllib2,re,json,time,argparse
import Queue
def getHtml(url,ref = None):
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/601.7.8')

        if ref:
        	request.add_header('Referer',ref)
        try:
        	page = urllib2.urlopen(request, timeout = 20)
        	html = page.read()
        	follows_json = json.loads(html)
        except:
			print 'time out wait 4 minute'
			#time.sleep(4*60)
			follows_json = {'errno':-1}
        return follows_json
		

class BaiDuPan(object):
	def  __init__(self):
	     self.request_queue=Queue.Queue(maxsize=20)

	def getShareList(self,uk,start):
		sharelists_url='http://yun.baidu.com/pcloud/feed/getsharelist?category=0&auth_type=1&request_location=share_home&start=%d&limit=60&query_uk=%d&channel=chunlei&clienttype=0&web=1' %(start,uk)
		ref = 'yun.baidu.com/share/home?uk= %d&view=share' %uk
		return getHtml(sharelists_url,ref)

	def getFollows(self,uk,start=0,limit=24):
		follows_url='http://yun.baidu.com/pcloud/friend/getfollowlist?query_uk=%d&limit=%d&start=%d&bdstoken=d82467db8b1f5741daf1d965d1509181&channel=chunlei&clienttype=0&web=1'%(uk,limit,start)
		ref='http://yun.baidu.com/pcloud/friendpage?type=follow&uk=%d&self=1'%uk
		return getHtml(follows_url,ref)

	def getFans(self,uk,start=0,limit=24):
		fans_url='http://yun.baidu.com/pcloud/friend/getfanslist?query_uk=%d&limit=%d&start=%d'%(uk,limit,start)
		return getHtml(fans_url)

	def start(self):
		follow_json = self.getFollows(2618821491,0)
		print(34444)
		print(follow_json)





baidu = BaiDuPan()
baidu.start()
