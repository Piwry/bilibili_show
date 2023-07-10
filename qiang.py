"""
用来蹲退票的
只要不放弃，困难总比办法多（
"""
import datetime
import time
import pyttsx3
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

engine = pyttsx3.init()
buy_url = "https://show.bilibili.com/platform/detail.html?id=73710&from=pc_ticketlist"

# 加载配置文件
with open('./cookie.json', 'r') as f:
    config = json.load(f)


def voice(message):
    engine.setProperty('volume', 1.0)
    engine.say(message)
    engine.runAndWait()
    engine.stop()
    voice(message)

# 设置抢购时间
TargetTime = "2013-10-3 8:00:00.00000000"

WebDriver = webdriver.Chrome()
wait = WebDriverWait(WebDriver, 0.5)
if len(config["bilibili_cookies"]) == 0:
    print("请运行 getcookiee.py 设置 cookie")
    exit(0)
else:
    WebDriver.get(
        buy_url)  # 输入目标购买页面
    for cookie in config["bilibili_cookies"][0]:
        WebDriver.add_cookie(
            cookie
        )
    WebDriver.maximize_window()
    WebDriver.refresh()



while True:
    try:
        # 等待抢票按钮出现并可点击
        element = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'product-buy.enable')))
        # 点击抢票按钮
        element.click()

        print("进入购买页面成功")
        break
    except:
        WebDriver.refresh()
        continue

element1 = None
element = None
while True:
    try:
        # 我其实不是很懂这个复选框，通过 f12 查看它的 class 勾上后会 'check-icon checked' 变但是只有这个 'check-icon' 能搜到
        element1 = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'check-icon')))
        break
    except:
        continue
while True:
    try:
        # 加个 until 能防止无效点击？还在学
        # until 影响效率所以先 find 一次
        element =WebDriver.find_element(By.CLASS_NAME, "confirm-paybtn.active")
        element =wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'confirm-paybtn.active')))
        element.click()
        break
    except:
        print("找不到")
        element1.click()
        continue

print("订单创建完成，请在一分钟内付款")
voice('快付款捏捏捏')
# 语音提醒时间
time.sleep(1145)