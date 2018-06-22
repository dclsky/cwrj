#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: dcl
# date: 2017/12/6


from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.c// 此行代码用来定位当前页面

browser.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[3]/div[4]/h3/a").click()
time.sleep(5)
