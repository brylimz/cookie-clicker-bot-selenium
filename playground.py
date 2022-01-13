from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("price_inside_buybox")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# abc = driver.find_element_by_css_selector(".documentation-widget a")
# print(abc.text)

# abc = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[1]/div[3]/h2')
# print(abc.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_times:
#     # print(time.text)
#     b = time.text
#     print(b)
events = {}

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

driver.close()
driver.quit()
