from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/cookieclicker/")

clicker = driver.find_elements(By.ID, "bigCookie")


def bot():
    for i in clicker:
        i.click()


looping = True
while looping:
    bot()
