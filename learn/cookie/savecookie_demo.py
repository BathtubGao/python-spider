import urllib.request
import http.cookiejar

# 设置保存cookie的文件，同级目录下的cookie.txt
filename = 'E:\PyCharm\python-spider\learn\cookie\cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
# 利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib.request.build_opener(handler)
# 此处的open方法同urlopen方法，也可以传入request
response = opener.open('https://www.zhihu.com/')
# 保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)