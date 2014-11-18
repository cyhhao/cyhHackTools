import cookielib
import urllib
import urllib2

__author__ = 'cyh'

if __name__ == '__main__':
    req = urllib2.Request(url="http://baidu.com")
    dic = {"qwe": "123", "aaa": "qadf"}
    for key in dic:
        req.add_header(key, dic[key])
    req.add_header("qwe", "asd")
    print req.headers


class net():
    User_Agent_360jisu = r"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"

    def __init__(self, Cookie="", User_Agent=User_Agent_360jisu, ):
        self.opener = urllib2.build_opener()
        self.cj = cookielib.CookieJar()
        self.cookie = Cookie
        self.header = {}
        self.User_Agent = User_Agent
        if Cookie != "":
            self.header['cookie'] = Cookie


    def __setUser_Agent(self, req, cont):
        req.add_header("User_Agent", cont)

    def setHeader(self, header):
        self.header = header

    def __addHeaders(self, req, header):
        for key in header:
            req.add_header(key, header[key])


    def Get(self, url, data={}, cookie=True, ):
        if cookie:
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
            urllib2.install_opener(self.opener)

        get_data = urllib.urlencode(data)
        print url + "?" + get_data
        req = urllib2.Request(url=url + "?" + get_data)
        self.__addHeaders(req, self.header)
        self.__setUser_Agent(req, self.User_Agent)

        res = self.opener.open(req)

        return res.read()

    def Post(self, url, data={}, cookie=True, ):
        if cookie:
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
            urllib2.install_opener(self.opener)

        post_data = urllib.urlencode(data)

        req = urllib2.Request(url=url, data=post_data)
        self.__addHeaders(req, self.header)
        self.__setUser_Agent(req, self.User_Agent)

        res = self.opener.open(req)

        return res.read()

