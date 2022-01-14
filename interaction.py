from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# FIRST STEP
# total = driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
# for n in total:
#     print(n.text)
total = driver.find_elements(By.CSS_SELECTOR, "#articlecount a")
for n in total[0:1]:
    print(n.text)