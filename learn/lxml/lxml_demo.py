from lxml import etree
html = etree.parse('hello.html')
#result = html.xpath('//li/@class')
result = html.xpath('//*[@class="bold"]')
print(result)
