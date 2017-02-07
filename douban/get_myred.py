import requests

# 浏览器请求头
loginHeaders = {
    'Host': 'accounts.douban.com',
    'Connection': 'keep-alive',
    'Content-Length': '118',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://accounts.douban.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://accounts.douban.com/popup/login?source=fm&use_post_message',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
loginData = {'source': 'fm', 'referer': 'https://douban.fm/', 'ck': '', 'name': '18994076185',
             'password': '*****', 'captcha_solution': '', 'captcha_id': ''}

# 处理cookie
f = open(r'E:\PyCharm\python-spider\douban\cookies.txt', 'r')
cookies={}
for line in f.read().split(';'):
    # 其设置为1就会把字符串拆分成2份
    name, value = line.strip().split('=', 1)
    cookies[name] = value
loginUrl = 'https://accounts.douban.com/j/popup/login/basic'
loginReq = requests.post(loginUrl, data=loginData, headers=loginHeaders, cookies=cookies, verify=False)
print(loginReq.text)
# redheartHeaders = {
#     'Host': 'douban.fm',
#     'Connection': 'keep-alive',
#     'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
#     'X-Requested-With': 'XMLHttpRequest',
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Referer': 'https://douban.fm/mine',
#     'Accept-Encoding': 'gzip, deflate, sdch, br',
#     'Accept-Language': 'zh-CN,zh;q=0.8'
# }
# redheartUrl = 'https://douban.fm/j/v2/redheart/basic?updated_time=2015-01-01+00%3A00%3A00'
# result = requests.post(redheartUrl, headers=redheartHeaders, cookies=loginReq.cookies)
# print(result.text)