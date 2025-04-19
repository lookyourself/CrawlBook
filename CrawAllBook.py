# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 11:48:42 2025
功能：抓住整个书城中所有书
步骤：
    1. 从首页获取所有书的链接
    2. 调用抓每本书的链接，调用crawOne(theBookUrl)
@author: 张治王朝
"""
import CrawOneBook_better
if __name__ == "__main__":
    url = "https://www.bibie.cc/html/"
    for rank in range(80):
        CrawOneBook_better.CrawOneBook(url + str(rank+1) + '/')