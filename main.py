from selenium import webdriver
from pyvirtualdisplay import Display



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

abc = driver.find_element_by_css_selector(".documentation-widget a")
print(abc.text)



driver.close()
driver.quit()
