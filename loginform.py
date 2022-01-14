from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


def robot():
    chrome_driver_path = "c:\development\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("http://secure-retreat-92358.herokuapp.com/")
    fname = driver.find_elements(By.NAME, "fName")
    abc = random.randint(1, 1000)
    dbc = random.randint(5, 1000)
    for n in fname:
        n.send_keys(abc)

    lname = driver.find_elements(By.NAME, "lName")
    for n in lname:
        n.send_keys(dbc)

    email = driver.find_elements(By.NAME, "email")
    for i in email:
        i.send_keys(f"jackjaggeriv{abc}@gmail.com")

    submit = driver.find_elements(By.CSS_SELECTOR, "form button")
    for n in submit:
        n.click()


Loop = True
while Loop:
    robot()
