import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CnnSpider(scrapy.Spider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    # Get all urls (special case: because we can write the url by ourselves)

    url_list = []

    # 0. Trial: For testing the code, see if it works well
    # for x, y in zip(range(0, 50, 10), range(1, 6)):
    #     temp = 'https://edition.cnn.com/search?q=microsoft&from=' + str(x) + '&size=10&page=' + str(
    #         y) + '&sort=newest&types=article&section='
    #     url_list.append(temp)

    # 1. Microsoft article business
    # for x, y in zip(range(0, 2360, 10), range(1 , 236)):
    #     temp = 'https://edition.cnn.com/search?q=microsoft&from=' + str(x) + '&size=10&page=' + str(
    #         y) + '&sort=newest&types=article&section=business'
    #     url_list.append(temp)

    # 2. All article business
    # Rule: page: from_page : results = 1: 0: 10 = 2: 10: 20
    for x, y in zip(range(0, 46510, 10), range(1 , 4652)):
        temp = 'https://edition.cnn.com/search?q=&from=' + str(x) + '&size=10&page=' + str(
            y) + '&sort=newest&types=article&section=business'
        url_list.append(temp)

    start_urls = url_list

    def parse(self, response):
        temp = {}


        # 0. Open the browser
        # need to unzip the chromedriver to the python folder first
        driver = webdriver.Chrome()
        driver.get(response.url)

        # time.sleep is important, it can let us wait for the loading to complete
        # You'll get nothing if you don't set it
        time.sleep(2)

        # WTF: the space ' ' in the class_name should be replaced by '.'
        # element = driver.find_elements(By.CLASS_NAME, "container__link.__link")

        # 1. Get the data (title, datetime, content)
        temp_title = driver.find_elements(By.CLASS_NAME, "container__headline.__headline")
        temp_datetime = driver.find_elements(By.CLASS_NAME, "container__date.__date.inline-placeholder")
        temp_content = driver.find_elements(By.CLASS_NAME, "container__description.__description.inline-placeholder")

        for x, y, z in zip(temp_title, temp_datetime, temp_content):
            temp['title'] = x.text
            temp['datetime'] = y.text
            temp['content'] = z.text

            yield temp

        # time.sleep(1)
        driver.quit()

# title: container__headline __headline
# datetime: container__date __date inline-placeholder
# content: container__description __description inline-placeholder
