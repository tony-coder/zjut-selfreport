#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
from pyvirtualdisplay import Display

# 打卡时间 小时、分钟
c_minute = "30"
c_hour = "00"

# 网址、用户名、密码
url = 'http://mapp.zjut.edu.cn/_web/_apps/eform/onlinesurvey/onlineSurvey_m.jsp?domainId=1&topicId=17&iportal.uid=124663'
username = '用户名'
password = '密码'


def work():
    try:
        display = Display(visible=0, size=(800, 600))
        display.start()
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        # 刚刚解压的chromedriver路径
        browser = webdriver.Chrome(
            "/root/chromedriver_linux64/chromedriver", chrome_options=options)

        browser.get(url)
        # 等待2s
        time.sleep(6)
        # 登录验证
        browser.find_element_by_id('username').clear()
        browser.find_element_by_id('username').send_keys(username)
        browser.find_element_by_id('password').clear()
        browser.find_element_by_id('password').send_keys(password)  # password
        browser.find_element_by_class_name('sl-login-btn').click()
        browser.find_element_by_class_name('l-btn-text').click()
        # 等待2s
        time.sleep(2)
        browser.find_element_by_link_text('提交').click()
        browser.find_element_by_class_name('l-btn-text').click()

        time.sleep(2)
        # 清空cookies
        browser.delete_all_cookies()

        # 退出浏览器
        time.sleep(2)
        browser.quit()
        logging.debug(time.strftime('%Y-%m-%d %H:%M:%S',
                                    time.localtime()) + ": Clock Success!")
        display.stop()
    except Exception as e:
        logging.debug(e)
        logging.debug(time.strftime('%Y-%m-%d %H:%M:%S',
                                    time.localtime()) + ": Clock Filed!")
        # 清空cookies
        browser.delete_all_cookies()
        time.sleep(2)
        browser.quit()
        display.stop()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        filename='debug.log',
                        filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                        # 日志格式
                        )
    # 添加任务
    scheduler = BlockingScheduler()
    # 设置定时任务时间
    scheduler.add_job(work, 'cron', minute=c_minute, hour=c_hour)
    logging.debug(time.strftime('%Y-%m-%d %H:%M:%S',
                                time.localtime()) + ": Add Task Work!")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
