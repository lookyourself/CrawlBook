# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 15:17:30 2025

@author: 张治王朝
"""
'''
总体流程
    1. 获取所有章节url √
    2. 爬取章节下文本信息 √
    3. 将一个章节所有数据输入txt文件中 √
    4. 封装为一个函数，调用书的首页链接，则可以创建对应文件夹，文件夹下有对应所有文件√
进度：
    2. 爬取章节下文本信息
        1. 拆解出文本数据
            1. 问题分析
                1. <div>直接层含有内容，指定子标签内容获取
            2. 方法
                1. 子标签筛选，文本标签也算
        2. 文本放在列表中，逐个输出到文本
            1. 问题
                1. 文本编码有问题  
    3. 输出到txt文件中
        1. 标题拆解获取，*获取中间
        2. 列表->str
            1. join函数
        3. 路径：绝对路径，后面调整为相对
                
方法：
    1. 利用Session
'''
import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup, NavigableString
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def CrawOneBook(webUrl):
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        })
    #webUrl = 'https://www.bibie.cc/html/36238/'
    response = session.get(webUrl, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select_one("title").text.split("最新")[0]
    introduce = soup.select_one(".intro").text.rsplit("！",1)[0] + "！"
    #获取本书所有url链接
    #link_url = soup.select_one(".listmain dd a")["href"]
    urlList = [url['href'] for url in soup.select(".listmain dd a") if url['href'].startswith("/") == True]

    for url in urlList:
        url = "https://www.bibie.cc/" + url
        #print(url)
        response = session.get(url, verify=False)

        soup = BeautifulSoup(response.text, 'html.parser')
        bookText = soup.select_one("#chaptercontent")
        head, *charptName, tail = soup.select_one("title").text.split("-")
        charptName = "".join(charptName)
        
        title_path = r'C:/tool/python/work/Crawler/file/BookCity/'+title+r'/'
        resultText = [book.encode('utf-8', errors='ignore').decode('utf-8') for book in bookText if isinstance(book,NavigableString)]
        os.makedirs(title_path, exist_ok=True)
        with open(title_path + charptName+".txt", "w", encoding="utf-8") as file:
            for index, line in enumerate(resultText):
                if(index < len(resultText)-2):
                    file.write(line + "\n")
        break;

if __name__ == "__main__":
    CrawOneBook('https://www.bibie.cc/html/1/')
    

# if __name__ == "__main__":
#     CrawOneBook('https://www.bibie.cc/html/1/')
    
#     session = requests.Session()
#     session.headers.update({
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#         })
#     webUrl = 'https://www.bibie.cc/html/36238/'
#     response = session.get(webUrl, verify=False)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     introduce = soup.select_one(".intro").text.rsplit("！",1)[0] + "！"
#     #获取本书所有url链接
#     link_url = soup.select_one(".listmain dd a")["href"]
#     urlList = [url['href'] for url in soup.select(".listmain dd a") if url['href'].startswith("/") == True]

#     for url in urlList:
#         url = "https://www.bibie.cc/" + url
#         #print(url)
#         response = session.get(url, verify=False)

#         soup = BeautifulSoup(response.text, 'html.parser')
#         bookText = soup.select_one("#chaptercontent")
#         head, *charptName, tail = soup.select_one("title").text.split("-")
#         charptName = "".join(charptName)
#         resultText = [book.encode('utf-8', errors='ignore').decode('utf-8') for book in bookText if isinstance(book,NavigableString)]
#         with open(r'C:\tool\python\work\Crawler\file\BookCity\蛊真人\\' + charptName+".txt", "w", encoding="utf-8") as file:
#             for index, line in enumerate(resultText):
#                 if(index < len(resultText)-2):
#                     file.write(line + "\n")
    