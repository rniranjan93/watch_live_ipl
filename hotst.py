from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
j=input()
i=int(input())
i=i-1
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
browser1 = webdriver.Chrome(chrome_options=chrome_options)
browser1.set_window_position(1000, 1000)
browser1.get(j)
time.sleep(4)
webdriver.ActionChains(browser1).send_keys("f").perform()
while(1):
    time.sleep(i*60+20)
    browser = webdriver.Chrome(r"C:\Users\Niranjan\Desktop\new\chromedriver.exe", chrome_options=chrome_options)
    browser.set_window_position(1000, 1000)
    browser.get(j)
    time.sleep(6)
    webdriver.ActionChains(browser).send_keys("f").perform()
    browser1.close()
    time.sleep(i*60+20)
    browser1 = webdriver.Chrome(r"C:\Users\Niranjan\Desktop\new\chromedriver.exe", chrome_options=chrome_options)
    browser1.set_window_position(1000, 1000)
    browser1.get(j)
    time.sleep(6)
    webdriver.ActionChains(browser1).send_keys("f").perform()
    browser.close()
