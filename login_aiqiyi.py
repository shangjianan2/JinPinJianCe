#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

import time

class login_aiqiyi:
    def __init__(self, driver, qq, pwd):
        self.driver = driver
        self.qq = qq
        self.pwd = pwd

    def login_with_QQ(self):
        self.call_loginDOC()
        self.exe_DOC()
        self.exe_QQ_login()


    def call_loginDOC(self):
        time.sleep(3)
        login1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/header/div/div/div[4]/div[6]')
        ActionChains(self.driver).move_to_element(login1).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/header/div/div/div[4]/div[6]/div[2]/div/div/div[3]/a[1]').click()


    def exe_DOC(self):
        time.sleep(1)
        switch_to_loginframe = self.driver.find_element_by_xpath('//iframe[@id="login_frame"]')
        self.driver.switch_to_frame(switch_to_loginframe)
        ZhangHaoMiMa = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[4]/div[2]/p/span/a[2]')
        ActionChains(self.driver).click(ZhangHaoMiMa).perform()
        time.sleep(1)
        QQ_login = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[5]/div[1]/div/div/a[3][@title="QQ"]')
        ActionChains(self.driver).click(QQ_login).perform()
        time.sleep(1)

    def exe_QQ_login(self):
        #切换到QQ登录窗口
        self.driver.switch_to_window(self.driver.window_handles[1])#切换到qq登录窗口
        QQ_frame_login = self.driver.find_element_by_xpath('//iframe[@id="ptlogin_iframe"]')#切换到登录界面
        self.driver.switch_to_frame(QQ_frame_login)
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@id="switcher_plogin"]').click()

        #输入密码并登录
        self.driver.find_element_by_xpath('//*[@id="u"]').send_keys(self.qq)
        self.driver.find_element_by_xpath('//*[@id="p"]').send_keys(self.pwd)
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()


if __name__ == '__main__':
    driver = webdriver.Firefox(firefox_profile='./profile', executable_path='./geckodriver1.exe')#geckodriver的最新版本

    driver.implicitly_wait(30)#设置加载driver加载元素时所等待的最长的时间，
    driver.get("https://www.iqiyi.com/v_19rr57hv5c.html")
    test = login_aiqiyi(driver, '1978707987', '130103020152')
    test.login_with_QQ()

    print 'login_aiqiyi test over'
