import urllib.request

req = urllib.request.Request('http://blog.csdn.net/cqcre')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)