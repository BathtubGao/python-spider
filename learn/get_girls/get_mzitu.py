import requests
from bs4 import BeautifulSoup
import os

class mzitu():

    # 调用request函数把套图地址传进去会返回给我们一个response
    def request(self,url):
        headers = {'User-Agent': "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                         "Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content

    # 这个函数是处理套图地址获得图片的页面地址
    def html(self, href):
        html = self.request(href)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)

    # 这个函数处理图片页面地址获得图片的实际地址
    def img(self, page_url):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    # 这个函数保存图片
    def save(self, img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    # 这个函数创建文件夹
    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("F:\mzitu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹')
            os.makedirs(os.path.join("F:\mzitu", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    def all_url(self, url):
        html = self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a[-3:-1]:
            title = a.get_text()
            print(u'开始保存:', title)
            path = str(title).replace("?", '_')
            self.mkdir(path)
            os.chdir("F:\mzitu\\" + path)
            href = a['href']
            self.html(href)

Mzitu = mzitu()
Mzitu.all_url('http://www.mzitu.com/all')