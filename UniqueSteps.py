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

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user_login').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def get_sequences(self, id, type):
        temp = []
        cond = ""

        if type == 'f':
            cond = 'title="Failed"'
        elif type == 'p':
            cond = 'title="Passed"'
        elif type == 'ip':
            cond = 'title="In'
        elif type == 'na':
            cond = 'Applicable"'
        else:
            cond = 'Executed"'
        if id != 0:
            self.driver.get(self.urls[id])
        t.sleep(3)
        obj = self.driver.find_elements(By.XPATH, "//div[contains(@id,'outer_step')]")
        for i in obj:
            t1 = i.get_attribute('innerHTML').split()
            if t1[13] == cond or t1[14] == cond:
                temp.append(int(t1[1][9:-1]))
        self.sequences.append(temp)

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

# urls = [
#     'https://ottr.opentext.com/test_run/execute/14267484',
#     'https://ottr.opentext.com/test_run/execute/14267538'
# ]
# names = ['London', 'Singapore']
# username = os.getenv('OTTR_USERNAME')
# password = os.getenv('OTTR_PASS')
# a = CompareFails(urls, names)
# a.login(username, password)
#
# a.keep_awake(5)
# a.get_sequences(0,'p')
# # a.get_sequences(1, 'p')
# a.print_sequences(0)
# a.get_sequences(0, 'f')
# a.print_sequences(1)
# # a.print_sequences(1)
# # a.tally_sequences(0, 1)
#
#
# # a.keep_awake(10)
# a.close_driver()