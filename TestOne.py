# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 00:45:20 2018
@author: 武状元
"""
import requests
import json
import pandas as pd
import time
#https://heat.qq.com/index.php
#https://heat.qq.com/

def get_TecentData(count=4, rank=0):  # 先默认为从rank从0开始
    url = 'https://xingyun.map.qq.com/api/getXingyunPoints'
    paload = {'count': count, 'rank': rank}
    response = requests.post(url, json=paload)
    datas = response.json()
    time = datas["time"]  # 有了dict格式就可以根据关键字提取数据了，先提取时间
    locs = datas["locs"]  # 再提取locs（这个需要进一步分析提取出经纬度和定位次数）
    locss = locs.split(",")

    temp = []  # 搞一个容器
    for i in range(int(len(locss) / 3)):
        lat = locss[0 + 3 * i]  # 得到纬度
        lon = locss[1 + 3 * i]  # 得到经度
        count = locss[2 + 3 * i]

        if (2250 < int(lat) < 2300 and 11390 < int(lon) < 11400):
            temp.append([time, int(lat) / 100, int(lon) / 100, count])  # 容器追加四个字段的数据：时间，纬度，经度和定位次数

    result = pd.DataFrame(temp)  # 用到神器pandas，真好用
    result.dropna()  # 去掉脏数据，相当于数据过滤了
    result.columns = ['time', 'lat', 'lon', 'count']
    result.to_csv('TecentData.txt', mode='a', index=False)  # model="a",a的意思就是append，可以把得到的数据一直往TecentData.txt中追加


if __name__ == '__main__':
    while (1):  # 一直循环吧，相信我，不到一小时你电脑硬盘就要炸，大概速度是一分钟一百兆数据就可以爬下来
        for i in range(4):
            get_TecentData(4, i)  # 主要是循环count，来获取四个链接里的数据

