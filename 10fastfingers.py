from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://10fastfingers.com/typing-test/english")
find_words = driver.find_elements(By.CSS_SELECTOR, "div .highlight")
for i in find_words:
    i.send_keys(i)
    i.send_keys(Keys.SPACE)
