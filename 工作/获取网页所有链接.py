import re
import urllib.request


def getlink(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url).read()
    file = file.decode('utf-8')
    pattern = '*'
    link = re.compile(pattern).findall(file)
    # 去重
    # link = list(set(link))
    return link


url = "http://www.csair.com/"
linklist = getlink(url)
for link in linklist:
    print(link[0])

