# pa chong
import urllib
#import pymysql
from urllib.request import urlopen
from urllib import request
import json
import chardet
import re

'''
uk: 2736848922 2618821491(me) 325913312

'''

class spider:

    db = ""
    url = "http://pan.baidu.com/share/link?shareid=3685432306&uk=1798788396&from=hotrec"
    # https://pan.baidu.com/share/link?shareid=2109459878&uk=1112219283
    # https://pan.baidu.com/wap/link?uk=1112219283&shareid=2109459878
    db_host = "localhost"
    db_user = "root"
    db_pwd = "root"
    db_name = "searchPan"


    # http://pan.baidu.com/share/link?shareid=3685432306&uk=1798788396&from=hotrec
    # http://yun.baidu.com/pcloud/feed/getsharelist?auth_type=1&start={start}&limit=20&query_uk={uk}&urlid={id}
    # http://yun.baidu.com/pcloud/friend/getfollowlist?query_uk={uk}&limit=20&start={start}&urlid={id}
    # http://yun.baidu.com/pcloud/friend/getfanslist?query_uk={uk}&limit=20&start={start}&urlid={id}

   # headers = map[string]
   # string
   # {
   #     "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HTC D820u Build/KTU84P) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baidubrowser/5.3.4.0 (Baidu; P1 4.4.4)",
   #     "Referer": "https://yun.baidu.com/share/home?uk=325913312#category/type=0"}

    '''
     获取用户订阅 存
    '''
    def getFollower(self, uk = 2618821491, limit = 20, start = 0):
        follow_url = "http://yun.baidu.com/pcloud/friend/getfollowlist?query_uk=%d&limit=%d&start=%d&bdstoken=e6f1efec456b92778e70c55ba5d81c3d&channel=chunlei&clienttype=0&web=1&logid=MTQ3NDA3NDg5NzU4NDAuMzQxNDQyMDY2MjA5NDA4NjU="%(uk, limit, start)
        # re = urlopen("http://yun.baidu.com/pcloud/friend/getfollowlist")
        # print(re)
        # return
        referer = "https://yun.baidu.com/share/home?uk=%d#category/type=0"%(uk)
        data = self.httpGet(follow_url, referer)

    '''
        获取用户粉丝
    '''
    def getFans(self, uk = 2736848922, limit = 20, start = 0):
        fans_url = "http://pan.baidu.com/pcloud/friend/getfanslist?query_uk=%s&limit=%d&start=%s&bdstoken=null&channel=chunlei&clienttype=0&web=1&logid=MTQ3NDAzNjQwNzg3OTAuNzM1MzMxMDUyMDczMjYxNA=="%(uk, limit, start)
        referer = "https://yun.baidu.com/share/home?uk=%d#category/type=0" % (uk)
        data = self.httpGet(fans_url, referer)

    '''
        获取用户分享
    '''
    def getShare(self, uk = 2618821491, limit = 20, start = 0):
        share_url = "http://pan.baidu.com/pcloud/feed/getsharelist?t=1474202771918&category=0&auth_type=1&request_location=share_home&start=%d&limit=%d&query_uk=%d&channel=chunlei&clienttype=0&web=1&logid=MTQ3NDIwMjc3MTkxOTAuMzA1NjAzMzQ4MTM1MDc0MTc=&bdstoken=e6f1efec456b92778e70c55ba5d81c3d"%(start, limit, uk)
        referer = "http://125.la/thread-13907804-1-1.html"
        data = self.httpGet(share_url, referer)

    '''
     HTTP GET
    '''
    def httpGet(self, url, referer):
        req = request.Request(url)
        req.add_header("Referer", referer)
        req.add_header("Cookie", "BAIDUID=051EC32730679E51970718104CC16E34:FG=1; BIDUPSID=051EC32730679E51970718104CC16E34; PSTM=1458559356; __cfduid=def9436786194ad595d2da10ac8d1c1311460883577; locale=zh; PSINO=6; H_PS_PSSID=1427_19034_21108_18559_22035_22174_22157")
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.add_header("Accept-Encoding", "gzip, deflate, sdch")
        req.add_header("Accept-Language", "en-US,en;q=0.8")
        req.add_header("Cache-Control", "max-age=0")
        req.add_header("Connection", "keep-alive")
        req.add_header("Host", "yun.baidu.com")
        req.add_header("Upgrade-Insecure-Requests", "1")
        req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")
        response = urllib.request.urlopen(req)
        lines = response.readlines()
        # line = response.readline()
        # print(chardet.detect(line))
        # print(response.headers["content-type"])
        # lcode = line.decode("ISO-8859-8")
        
        for line in lines:
            # new_line = line.encode('raw_unicode_escape')
            print(chardet.detect(line))
        # print(chardet.detect(lines))
        print("end")

    """
     获取内容
    """
    def getContent(self):
        response = urlopen(self.url)
        line = response.readlines()
        line = response.readline()
        line = response.read()
        print(line)

    def connectDb(self):
        self.db = pymysql(self.db_host, self.db_user, self.db_pwd, self.db_name)

    def select(self):
        self.connectDb()
        cursor = self.db.cursor()
        sql = "select * from pan_user"
        cursor.execute(sql)
        data = cursor.fetchone()
        print(data)

    def getCursor(self):
        if self.db:
            self.connectDb()
        self.cursor = self.db.cursor()

    def closeDb(self):
        self.db.close()

    def query(self, sql):
        if self.curosr:
            self.getCursor()
        self.cursor.execute(sql)

    def fetchOne(self):
        return self.cursor.fetchone()

    def fetchAll(self):
        return self.cursor.fetchall()

    def regHtml(self, html):
        print(html)

instance = spider()
# instance.select()
# instance.getFollower()
# instance.getFans()
instance.getShare()

'''
req = urllib.request.Request("http://baidu.com/")
req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")
req.add_header("Connection", "keep-alive")
req.add_header("Accept-Encoding", "gzip, deflate, sdch")
re = urlopen(req, None, 60);
print(re.read())
'''
'''
只需替换链接中uk,shareid或者album_id即可访问
分享专辑链接类型：https://pan.baidu.com/wap/album/info?uk=1112219283&album_id=129732510768224935
普通文件或者文件夹类型：https://pan.baidu.com/wap/link?uk=1112219283&shareid=2109459878
最近在找实习工作,有点无聊,没事搞,研究了下爬百度网盘的用户分享
获取用户订阅:
http://yun.baidu.com/pcloud/friend/getfollowlist?query_uk=%s&limit=24&start=%s&bdstoken=e6f1efec456b92778e70c55ba5d81c3d&channel=chunlei&clienttype=0&web=1&logid=MTQ3NDA3NDg5NzU4NDAuMzQxNDQyMDY2MjA5NDA4NjU=
(query_uk limit start是必须参数)
获取用户粉丝:
http://pan.baidu.com/pcloud/friend/getfanslist?query_uk=%s&limit=24&start=%s&bdstoken=null&channel=chunlei&clienttype=0&web=1&logid=MTQ3NDAzNjQwNzg3OTAuNzM1MzMxMDUyMDczMjYxNA== (query_uk limit start是必须参数)
获取用户分享:
http://pan.baidu.com/pcloud/feed/getsharelist?t=1474202771918&category=0&auth_type=1&request_location=share_home&start=0&limit=60&query_uk=224534490&channel=chunlei&clienttype=0&web=1&logid=MTQ3NDIwMjc3MTkxOTAuMzA1NjAzMzQ4MTM1MDc0MTc=&bdstoken=e6f1efec456b92778e70c55ba5d81c3d
(query_uk limit start auth_type是必须参数)
上面3个连接请求必须带上Referer("Referer", "https://yun.baidu.com/share/home?uk=23432432#category/type=0"),
否则请求不到json数据, 获取用户订阅和获取用户粉丝每次请求一次休眠2s的话可以无限制请求,对ip没要求,获取用户分享超坑,一个ip只能请求10次,并且休眠也没用.
因为没有那么多ip,我就去研究手机版的用户分享,手机版获取用户分享可以一次性连续请求60次,60次后必须休眠35s左右在继续请求就可以,
不会像pc版那样必须换ip, 但是手机版只能请求网页源码,然后用正则进行匹配.
手机版分享: http://pan.baidu.com/wap/share/home?uk=2889076181&start=%s&adapt=pc&fr=ftw (uk:每个百度网盘用户的唯一标示,start:用户可能有上百上千个分享,必须分页,start默认从0开始,手机版默认分页是20个每页)
'''
