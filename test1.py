#!/usr/bin/python
# -*- coding: UTF-8 -*-
#案例：Selenium的ID定位法。通过html元素的id属性来定位html元素！
'''
案例需求：
  1). 打开注册A.html页面，使用id定位，自动填写(账号A：admin、密码A:123456)
  2). 填写完毕后，3秒钟关闭浏览器窗口
'''
#注意：运行时，无需保证火狐浏览器是运行状态的！
from time import sleep
from selenium import webdriver
driver=webdriver.Firefox()
url="C:\\A\\注册A.html" #OK
driver.get(url)
user=driver.find_element_by_id("userA")
user.send_keys("admin")
pwd=driver.find_element_by_id("passwordA")
pwd.send_keys("123456")
sleep(3) #Pycharm小技巧：鼠标放在要导包的代码上，按CTRL+ALT+空格来自动导包
driver.quit()