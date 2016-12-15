import urllib.request
import http.cookiejar

# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib.request.build_opener(handler)
# 此处的open方法同urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

