#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, requests
from selenium import webdriver

url_site= 'https://www.ascribe.io/app/login'
navigator= webdriver.Firefox()
navigator.get(url_site)
response = requests.get(url_site)

user = "your username"
passwd = "your pass"

field_username = navigator.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div/div/input")
field_username.send_keys(user)
time.sleep(1)

field_password = navigator.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/form/div[3]/div/div/div/div/input")
field_password.send_keys(passwd)
time.sleep(1)

button_login = navigator.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/form/div[4]/div[2]/button")
button_login.click()
time.sleep(5)
