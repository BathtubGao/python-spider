import urllib.request

data = urllib.request.urlopen("http://www.baidu.com").read()
data = data.decode('UTF-8')
print(data)