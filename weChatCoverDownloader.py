import requests
import re
import urllib.request

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def articleTitle(html):
    pattern1 = re.compile('var msg_title = ".*"')
    result1 = pattern1.findall(html)[0]

    return result1.lstrip('var msg_title = "').rstrip('"')

def imgURL(html):
    pattern1 = re.compile('var msg_cdn_url = ".*=jpeg"')
    result1 = pattern1.findall(html)[0]

    pattern2 = re.compile('http.*jpeg')
    result2 = pattern2.findall(result1)[0]

    return result2

def main():
    url = input("请粘贴要下载封面的公众号文章链接：\n")
    html = getHTMLText(url)

    img = urllib.request.urlopen(imgURL(html)).read()

    with open(articleTitle(html) + ' - 封面.jpg', 'wb') as f:
        f.write(img)

main()
