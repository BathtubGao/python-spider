import urllib
import http.cookiejar

filename = 'E:\PyCharm\python-spider\learn\cookie\cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
values = {'username': 'chebao', 'password': 'chebao123'}
postdata = urllib.parse.urlencode(values).encode('utf-8')
loginUrl = 'http://testmanage.chebao.com.cn/CheBao/CheBao/login/userLogin'
result = opener.open(loginUrl, postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
gradeUrl = 'http://testmanage.chebao.com.cn/CheBao/main.jsp'
result = opener.open(gradeUrl)
print(result.read().decode('utf-8'))