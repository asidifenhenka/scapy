# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from wxapp.items import WxappItem


class WxappApiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'),follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'),callback='parse_detail',follow=False)
    )

    def parse_detail(self, response):
        text = response.text
        soup = BeautifulSoup(text,'lxml')

        titles = soup.find_all('h1',class_='ph')
        times = soup.find_all('span',class_='time')
        authors = response.xpath("//p[@class='authors']")
        author = authors.xpath(".//a/text()").get()
        print(author)
        for i in titles:
            title = i.get_text().strip()
            print(title)
        for j in times:
            time = j.get_text().strip()
            print(time)
        item = WxappItem(title=title,author=author,time=time)
        yield item