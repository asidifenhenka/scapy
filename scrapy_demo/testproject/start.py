#coding=utf8
from scrapy import cmdline


cmdline.execute("scrapy crawl test_spider".split()) #列表化

'''等价于'''

# cmdline.execute(['scrapy','crawl','qsbk_spider'])