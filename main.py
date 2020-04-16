from selenium import webdriver
import time

class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.pw = pw
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

InstaBot(input('Enter username: '), input('Enter password: '))