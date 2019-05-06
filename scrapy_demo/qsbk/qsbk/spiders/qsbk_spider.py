# -*- coding: utf-8 -*-
import scrapy
from items import QsbkItem
from bs4 import BeautifulSoup


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/2/']
    def parse(self, response):
        text = response.text
        soup = BeautifulSoup(text,'lxml')
        print(text)
        articles = soup.find_all('article',class_='item')
        for a in articles:
            contents = a.find_all('a',class_='text')
            authors = a.find_all('a',class_='username')
            for i in contents:
                content = i.get_text().strip()
            for j in authors:
                author = j.get_text()

            item = QsbkItem(author=author,content=content)
            # duanzi = {'author':author,'content':content}
            yield item




