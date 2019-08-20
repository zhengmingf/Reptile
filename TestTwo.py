# -*- coding:utf-8 -*-
#作者:猫先生的早茶
#时间:2019年5月19日
import requests
from lxml import etree
import os


"""
设置浏览器头部，
User-Agent用于表示浏览器的参数信息
Referer用于设置使用那个网页跳转过来的
url用于设置网址模板，可以通过.format参数补充网址
"""
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0",
          "Referer":"https://www.mzitu.com/jiepai/comment-page-1/",}
url = 'https://www.mzitu.com/jiepai/comment-page-{}/#comments'
name = 0

def get_html(url):
    """获取网页代码并以返回值的形式弹出"""
    html = requests.get(url,headers=header).text
    return html

def get_url(html):
    """获取图片链接并以返回值的形式弹出"""
    etree_html = etree.HTML(html)
    img_url = etree_html.xpath('//img[@class="lazy"]/@data-original')
    return img_url

def get_img(url):
    """下载图片并保存到指定文件夹下"""
    global  name
    name += 1
    img_name = 'static\\image\\{}.jpg'.format(name)
    img = requests.get(url,headers=header).content
    with open(img_name,'wb') as save_img:
        save_img.write(img)


if __name__ == '__main__':
    '''使用for循环爬取所有网页'''
    for n in range(1,2):
        print("正在爬取第{}页".format(n))
        html = get_html(url.format(n))
        img_list = get_url(html)
        for img in img_list:
            get_img(img)


