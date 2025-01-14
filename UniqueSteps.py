# Logging in to OTTR and opening a testing page
# Prints all my failed test cases as a dict
# Compares with someone else's fails and prints out what is unique to each of us

# To do
#--------
# Fix for not executed
# Change the variables urls and names to make it just urls = [(url, name)...]
import os

from dotenv import load_dotenv
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By

# load_dotenv()
class UniqueSteps:
    def __init__(self, urls, names):
        self.driver = webdriver.Chrome()
        self.driver.get(urls[0])
        self.urls = urls
        self.sequences = []
        self.driver.implicitly_wait(10)
        self.names = names
        self.passed = []
        self.failed = []
        self.na = []
        self.ip = []
        self.ne = []

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user_login').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def get_sequences(self, idx):
        temp_pass = []
        temp_fail = []
        temp_na = []
        temp_ne = []
        temp_ip = []
        index = 1
        if idx != 0:
            self.driver.get(self.urls[idx])
        t.sleep(3)
        obj = self.driver.find_elements(By.XPATH, "//div[contains(@id, 'outer_step')]")
        for i in obj:
            temp = i.find_element(By.XPATH, ".//img").get_attribute("title")
            if temp == 'Passed':
                temp_pass.append(index)
            elif temp == 'Failed':
                temp_fail.append(index)
            elif temp == 'Not Applicable':
                temp_na.append(index)
            elif temp == 'Not Executed':
                temp_ne.append(index)
            elif temp == 'In Progress':
                temp_ip.append(index)
            index += 1
        self.passed.append(temp_pass)
        self.failed.append(temp_fail)
        self.na.append(temp_na)
        self.ne.append(temp_ne)
        self.ip.append(temp_ip)

    def print_sequences(self, index):
        print(self.sequences[index])
        # for x, i in enumerate(self.fails[index]):
        #     if self.fails[index][i] != 0:
        #         print(x, int(i[9:-1]))

    def tally_sequences(self, i1, i2):
        a1 = self.sequences[i1]
        a2 = self.sequences[i2]
        in_2_not_1 = []
        in_1_not_2 = []
        for i in a1:
            if i not in a2:
                in_1_not_2.append(i)
        for i in a2:
            if i not in a1:
                in_2_not_1.append(i)
        print("---------")
        print(self.names[i1], "vs", self.names[i2])
        print("unique to", self.names[i1], in_1_not_2)
        print("unique to", self.names[i2], in_2_not_1)
        print("---------")
        return in_1_not_2, in_2_not_1

    @staticmethod
    def keep_awake(seconds):
        t.sleep(seconds)

    def close_driver(self):
        self.driver.close()