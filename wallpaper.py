import os
import time
import requests
from bs4 import BeautifulSoup

# 获取图片网页并将网页中的图片下载到本地
def GetImages(url):
    html = requests.get(url,timeout=2).content.decode('gbk')
    soup = BeautifulSoup(html,"html.parser")
    images = soup.select('div.list li a img')
    for image in images:
        link = image['src']
        display = link.split('/')[-1]
        print('【+】正在下载：',display)
        filename = './images/'+display
        r = requests.get(link,timeout=10)
        with open(filename, 'wb') as f:
            f.write(r.content)
            f.close()
# 获取爬取的页数，并返回多少也输的网址
def GetUrls(page_links_list):
    pages = int(input("【+】请输入你想要爬取的页数："))
    if pages > 1:
        for page in range(1,pages+1):
            url = "http://www.netbian.com/index_" + str(page) + ".htm"
            page_links_list.append(url)
    else:
        page_links_list = page_links_list
# 主程序
if __name__ == '__main__':
    page_links_list = ['http://www.netbian.com/'] # 准备一个网址列表，第一个元素为首页
    GetUrls(page_links_list) # 开始获取要爬取页数的网址
    os.mkdir('./images') # 使用os模块创建目录
    print("【+】开始下载。")
    start = time.time() # 获取程序开始执行时间
    for url in page_links_list:
        GetImages(url)
    print("【+】图片下载成功！")
    end = time.time() - start
    print(f'消耗时间为{end}')