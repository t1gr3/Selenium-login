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

# Copy css selector
filename = 'your path example - /root/desktop/image.pdf'
btn_test = navigator.find_element_by_css_selector(".file-drag-and-drop > input:nth-child(3)").send_keys(filename)
time.sleep(3)

field_artist = navigator.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/form/div[4]/div/div/div/div/input")
field_artist.send_keys("your data")
time.sleep(1)

field_title = navigator.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/form/div[5]/div/div/div/div/input")
field_title.send_keys("your title")
time.sleep(1)

field_year = navigator.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/form/div[6]/div/div/div/div/input")
field_year.send_keys("2017")
time.sleep(1)

button_load = navigator.find_element_by_xpath("//button[@class='btn btn-default btn-wide']")
button_load.click()
time.sleep(5)

navigator.save_screenshot('your file .png')
time.sleep(1)

navigator.quit()
