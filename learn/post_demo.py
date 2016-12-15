from urllib import request, parse

values = {'username': 'chebao', 'password': 'chebao123'}
login_data = parse.urlencode(values).encode('utf-8')
req = request.Request('http://testmanage.chebao.com.cn/CheBao/main.jsp')
data = request.urlopen(req, login_data).read()
data = data.decode('utf-8')
print(data)