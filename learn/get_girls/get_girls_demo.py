import requests
from bs4 import BeautifulSoup
import os

'''
参考地址：http://cuiqingcai.com/3179.html
'''

# 浏览器请求头
headers = {'User-Agent': "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                         "Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://www.mzitu.com/all'
# 使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容
# headers为上面设置的请求头、请务必参考requests官方文档解释
start_html = requests.get(all_url, headers=headers)
# 打印出start_html (请注意，concent是二进制的数据，
# 一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
# print(start_html.text)
# 使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）
Soup = BeautifulSoup(start_html.text, 'lxml')
# 使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）
# li_list = Soup.find_all('li')
# for li in li_list:
#    print(li)
# 只抓取前10页
all_a = Soup.find('div', class_='all').find_all('a')[:10]
for a in all_a:
    # 取出a标签的文本
    title = a.get_text()
    path = str(title).strip()
    isExists = os.path.exists(os.path.join("F:\mzitu", path))
    if not isExists:
        print(u'建了一个名字叫做', path, u'的文件夹')
        os.makedirs(os.path.join("F:\mzitu", path))
    else:
        print(u'名字叫做', path, u'的文件夹已经存在了！')
    os.chdir("F:\mzitu\\" + path)
    # 取出a标签的href属性
    href = a['href']
    html = requests.get(href, headers=headers)
    html_Soup = BeautifulSoup(html.text,'lxml')
    # 查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1, int(max_span)+1):
        page_url = href + '/' + str(page)
        img_html = requests.get(page_url, headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src']
        # 取URL倒数第四至第九位做图片的名字
        name = img_url[-9:-4]
        img = requests.get(img_url, headers=headers)
        # 写入多媒体文件必须要 b 这个参数！！必须要！！
        f = open(name+'.jpg', 'ab')
        # 多媒体文件要用content
        f.write(img.content)
        f.close()
