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
    User_Agent_FireFox = r"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
    User_Agent_IE11 = r"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko"
    User_Agent_Baidu = r"Baiduspider"
    User_Agent_Google = r"Googlebot"
    User_Agent_Chrome = r"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1653.0 Safari/537.36"

    def __init__(self, Cookie="", User_Agent=User_Agent_Chrome, headers={}):
        self.opener = urllib2.build_opener()
        self.cj = cookielib.CookieJar()
        self.cookie = Cookie
        self.header = headers
        self.User_Agent = User_Agent
        if Cookie != "":
            self.header['cookie'] = Cookie


    def __setUser_Agent(self, req, cont):
        req.add_header("User_Agent", cont)

    def setHeaders(self, headers):
        self.header = headers

    def setHeaders_fromStr(self, string):
        row = string.split('\n')
        for li in row:
            it = li.split(':')
            self.header[it[0]] = ''.join(it[1:])


    def setHeaders_fromFile(self, path):
        string = self.__readFromFile(path)
        self.setHeaders_fromStr(string)

    def setCookie_fromFile(self, path):
        string = self.__readFromFile(path)
        self.cookie = string

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

    def __readFromFile(self, path):
        fin = open(path)
        return fin.read()

    def __addHeaders(self, req, header):
        for key in header:
            req.add_header(key, header[key])


# def make_cookie(name, value):
# return cookielib.Cookie(version=0, name=name, value=value, port=None, port_specified=False, domain="xxxxx",
# domain_specified=True, domain_initial_dot=False, path="/", path_specified=True,
# secure=False, expires=None, discard=False, comment=None, comment_url=None, rest=None)
#
# jar = cookielib.CookieJar()
# jar.set_cookie(Cookielib)
#     jar.set_cookie(make_cookie("name", "value"))
