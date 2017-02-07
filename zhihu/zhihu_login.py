# https://github.com/lining0806/PythonSpiderNotes/tree/master/ZhihuSpider
# 注意切换使用python interpreter
import requests
import configparser

def create_session():
    cf = configparser.ConfigParser()
    cf.read('config.ini')
    cookies = cf.items('cookies')
    cookies = dict(cookies)
    from pprint import pprint
    pprint(cookies)
    email = cf.get('info', 'email')
    password = cf.get('info', 'password')
    session = requests.session()
    login_data = {'email': email, 'password': password}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/43.0.2357.124 Safari/537.36',
        'Host': 'www.zhihu.com',
        'Referer': 'http://www.zhihu.com/'
    }
    r = session.post('http://zhihu.com/login/email', data=login_data, headers=header)
    print(r)
    if r.json()['r'] == 1:
        print('Login Failed, reason is:')
        for m in r.json()['data']:
            print(r.json()['data'][m])
        print('So we use cookies to login in...')
        has_cookies = False
        for key in cookies:
            if key != '__name__' and cookies[key] != '':
                has_cookies = True
                break
            if has_cookies is False:
                raise ValueError('请填写config.ini文件中的cookies项。')
            else:
                r = session.get('http://www.zhihu.com/login/email', cookies=cookies)

        with open('E:\PyCharm\python-spider\zhihu\login.html', 'w') as fp:
            fp.write(r.content)

        return session, cookies



requests_session, requests_cookies = create_session()
url = 'http://www.zhihu.com/login/email'
print(13)
content = requests_session.get(url, cookies=requests_cookies).content
print(content)
with open('E:\PyCharm\python-spider\zhihu\login.html', 'w') as fp:
    fp.write(content)