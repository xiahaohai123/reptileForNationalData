from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


class Reptile:
    def __init__(self):
        self.name_list = []
        self.head_list = []
        self.data_list = []
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')

    def crawling(self, target_url, *click_xpaths):
        with webdriver.Chrome(options=self.options) as driver:
            wait = WebDriverWait(driver, 10)

            driver.get(target_url)
            for xpath in click_xpaths:
                driver.find_element_by_xpath(xpath).click()
                time.sleep(2)

            data_head = driver.find_element_by_xpath(
                '//*[@id="main-container"]/div[2]/div[2]/div[2]/div/div[1]/table/thead').get_attribute('innerText')
            #
            data_head = str(data_head).replace('\n', "").split('\t')
            del data_head[0]
            data_head.reverse()
            self.head_list = data_head

            data_body = driver.find_element_by_xpath(
                '//*[@id="main-container"]/div[2]/div[2]/div[2]/div/div[3]/table/tbody').get_attribute('innerText')
            rows = str(data_body).split('\n')
            self.name_list = []
            self.data_list = []
            for row in rows:
                data_list = row.split('\t')
                self.name_list.append(data_list[0])
                del data_list[0]
                temp_list = []
                for data in data_list:
                    temp_list.append(float(data))
                temp_list.reverse()
                self.data_list.append(temp_list)
