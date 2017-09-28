from selenium import webdriver
from time import sleep


aa=webdriver.Chrome()
aa.get("http://www.taobao.com")
sleep(6)

aa.quit()
