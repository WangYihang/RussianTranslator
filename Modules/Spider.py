#!/usr/bin/env python
# encoding:utf-8

import requests
import bs4
import sys


session = requests.Session()
session.headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"ru.yicool.cn",
        "Referer":"http://www.yicool.cn/",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

def handleAntiSpider(urls):
    global session


def getContent(url):
    global session
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except Exception, e:
        return str(e)

def createUrl(word):
    url = "http://ru.yicool.cn/"
    return url + word

def showHelp(scriptName):
    print "Usage : "
    print "        python %s [WORD]" % (scriptName)


def getMeaning(soup):
    print soup
    result = []
    div = soup.find("div", class_="part_main")
    print div
    temp = div.find("dl")
    temp = temp.find("dd")
    print temp
    for i in temp:
        if len(i) == 1: # 莫名其妙会出现空的对象
            continue
        for j in i:
            print j
    return result

def getWords(soup):
    result = []
    return result

def getSentences(soup):
    result = []
    return result


def getResult(soup):
    result = {}
    result["meaning"] = getMeaning(soup) # 释义
    result["words"] = getWords(soup) # 相关词组
    result["sentences"] = getSentences(soup) # 双语例句
    return result

def printResult(result):
    # 释义

    # 相关词组

    # 双语例句

    print result


def getUrls(soup):
    soup.getAll()

def main():
    if len(sys.argv) != 2:
        showHelp(sys.argv[0])
        exit(1)
    word = sys.argv[1]
    content = getContent(createUrl(word))
    soup = bs4.BeautifulSoup(content, "html.parser")
    urls = getUrls(soup)
    handleAntiSpider(urls)
    result = getResult(soup)
    printResult(result)


def unused():
    content = content.split("\n")
    for line in content:
        # print line
        if r"<span class='class1'>" in line:
            line = line.replace("<span class='class1'>", "")
            line = line.replace("<span class='class2'>", "")
            line = line.replace("</span>", "")
            line = line.replace("<li>", "")
            line = line.replace("</li>", "")
            line = line.replace("<b>", " ")
            line = line.replace("</b>", " ")
            line = line.replace("<br>", "")
            print line

if __name__ == "__main__":
    main()
