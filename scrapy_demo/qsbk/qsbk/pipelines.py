# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("daunzi.json","w",encoding='utf-8')
    def open_spider(self,spider):
        pass
    def process_item(self, item, spider):
        item_json = json.dumps(dict(item),ensure_ascii=False) + '\n'  # 在使用item时候 要注意转一下字典类型
        self.fp.write(item_json)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("end..............")

