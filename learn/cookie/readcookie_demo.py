import urllib.request
import http.cookiejar

# 创建MozillaCookieJar实例对象
cookie = http.cookiejar.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('E:\PyCharm\python-spider\learn\cookie\cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib.request.Request("https://www.zhihu.com/")
# 利用urllib的build_opener方法创建一个opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read())