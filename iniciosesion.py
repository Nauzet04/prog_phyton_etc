from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge("./msedgedriver.exe")
#driver.maximize_window()
driver.get("https://redcoatic.com/login/")
email ="franm9029@hotmail.com"
password= "Atlas123"
email_textfield = driver.find_element("id", ":r0:")
password_textfield = driver.find_element("id", ":r1:")
time.sleep(4)
#login_button = driver.find_element("button")
email_textfield.send_keys(email)
time.sleep(1)
password_textfield.send_keys(password)
time.sleep(1)

#login_button.click()