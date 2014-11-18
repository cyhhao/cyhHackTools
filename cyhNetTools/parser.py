# coding:utf-8
import sgmllib


__author__ = 'cyh'


class Split():
    def __init__(self, html):
        self.html = html

    def getWantTags(self,tag):
        class my(sgmllib.SGMLParser):
            def handle_starttag(self, tag, method, attrs):
                pass

            def handle_endtag(self, tag, method):
                pass

            def handle_data(self, data):
                print data

            def __int__(self, tagName=None, attrsList=None):
                self.tagName = tagName
                self.attrList = attrsList

        m = my()

        m.feed(self.html)


if __name__ == '__main__':
    pass
    # sp = Split("<a>123123<b>7</b><a>")
    # sp.getWantTags("a")
    # BeautifulSoup