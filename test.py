#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

import time
import login_aiqiyi
from video_play_aiqiyi import *

#driver = webdriver.Firefox(firefox_profile='./profile', executable_path='./geckodriver1.exe')#geckodriver的最新版本
driver = webdriver.Firefox(executable_path="./geckodriver")


driver.implicitly_wait(30)#设置加载driver加载元素时所等待的最长的时间，
driver.get("https://www.iqiyi.com/v_19rrdh6354.html")
#time.sleep(40)

time.sleep(5)
print 'start up'
test_login = login_aiqiyi.login_aiqiyi(driver, '1978707987', '130103020152')
test_login.login_with_QQ()
print 'has login'
time.sleep(4)
driver.save_screenshot('s3.png')
driver.switch_to_window(driver.window_handles[0])
driver.refresh()
print '1'
time.sleep(40)
print '2'
test_play = video_play_aiqiyi(driver)
test_play.play('GaoQing')
print '3'

driver.save_screenshot('s2_before.png')
time.sleep(10)
driver.save_screenshot('s2_afer.png')
driver.close()
driver.quit()
print 'game over'
