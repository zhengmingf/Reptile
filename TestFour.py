# -*- coding:utf-8 -*-
#作者：猫先生的早茶
#时间：2019年5月21日

import requests
from lxml import etree

#https://www.58pic.com/c/16029893


main_url = 'https://www.58pic.com/c/16029893'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
           'Referer':'https://www.58pic.com/piccate/10-0-0-p1.html',}

def get_html(url):
    '''下载网页代码'''
    html = requests.get(url,headers).text
    return html

def get_page_url(data):
    '''提取详情页url'''
    html = etree.HTML(data)
    url_list = html.xpath('//div[@class="card-img"]/a/@href')
    return url_list

def get_img_url(data):
    '''提取高清大图url'''
    html = etree.HTML(data)
    url = html.xpath('//div[@class="pic-box"]/img/@data-src')[0]
    title = html.xpath('//img[@class="show-area-pic"]/@title')[0]+'.jpg'
    return url,title

def get_img(url,file):
    '''下载图片'''
    file_name = 'picture\\'+file
    img = requests.get(url,headers=headers).content
    with open (file_name,'wb') as save_img:
        save_img.write(img)

# html = get_html(main_url)
# url_list = get_page_url(html)
# html = get_html('http:'+url_list[0])


html = get_html(main_url)
url_list = get_page_url(html)
for url in url_list:
    html = get_html('http:'+url)
    img_url,img_title = get_img_url(html)
    get_img('http:'+img_url,img_title)
    print ('正在下载{}'.format(img_title))