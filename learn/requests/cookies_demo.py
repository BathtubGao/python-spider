import requests

# 模拟登录，保留cookie
loginData = {'username': 'chebao', 'password': '******'}
loginReq = requests.post('http://testmanage.chebao.com.cn/CheBao/CheBao/login/userLogin', data=loginData)
mainReq = requests.post('http://testmanage.chebao.com.cn/CheBao/main.jsp', cookies=loginReq.cookies)
print(mainReq.text)