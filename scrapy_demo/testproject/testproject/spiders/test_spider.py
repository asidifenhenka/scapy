# -*- coding: utf-8 -*-
import scrapy
# from items import TestItem
from bs4 import BeautifulSoup

class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        text = response.text
        soup = BeautifulSoup(text)
        print(soup)
        quotes = soup.find_all('div',class_='quote')
        for quote in quotes:
            texts = quote.find_all('span',class_='text')
            for text in texts :
                text = text.get_text()
                print(text)
            tags = quote.find_all('a',class_='tag')
            for tag in tags:
                tag = tag.get_text()
                print(tag)
