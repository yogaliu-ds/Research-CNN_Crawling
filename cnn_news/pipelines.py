# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CnnNewsPipeline:

    def process_item(self, item, spider):
        # We get all items from the spider.
        # Here we need to store it to the csv or database.
        print('CNN_NEWS_PIPELINE', item['title'])
        return item
    