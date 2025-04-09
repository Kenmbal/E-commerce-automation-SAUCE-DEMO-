from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random

"""
 NEVER USE KEYS.ENTER IN FORM FIELDS
"""
options = Options()
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.saucedemo.com/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "user-name"))
) #find or locate the class before excuting the next code


input_element = driver.find_element(By.ID, "user-name") #you can use By.ID, "(name of the id)"
input_element.clear() #clear al the text in the text area
input_element.send_keys("standard_user") 

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "password"))
) #find or locate the class before excuting the next code

input_element = driver.find_element(By.ID, "password") #you can use By.ID, "(name of the id)"
input_element.clear() #clear al the text in the text area
input_element.send_keys("secret_sauce") 

login = driver.find_element(By.ID, "login-button")
login.click()

#input("Solve the CAPTCHA manually, then press Enter to continue...")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "item_4_title_link"))
) #find or locate the class before excuting the next code

item = driver.find_element(By.ID, "item_4_title_link")
item.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "add-to-cart"))
) #find or locate the class before excuting the next code

add = driver.find_element(By.ID, "add-to-cart")
add.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "shopping_cart_container"))
) #find or locate the class before excuting the next code

cart = driver.find_element(By.ID, "shopping_cart_container")
cart.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "checkout"))
) #find
checkout = driver.find_element(By.ID, "checkout")
checkout.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "first-name"))
) #find or locate the class before excuting the next code

first = driver.find_element(By.ID, "first-name") #you can use By.ID, "(name of the id)"
first.clear() #clear al the text in the text area
first.send_keys("Ken") 

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "last-name"))
) #find or locate the class before excuting the next code

input_element = driver.find_element(By.ID, "last-name") #you can use By.ID, "(name of the id)"
input_element.clear() #clear al the text in the text area
input_element.send_keys("Bal") 

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "postal-code"))
) #find or locate the class before excuting the next code

input_element = driver.find_element(By.ID, "postal-code") #you can use By.ID, "(name of the id)"
input_element.clear() #clear al the text in the text area
input_element.send_keys("4545") 

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "continue"))
) #find
cont = driver.find_element(By.ID, "continue")
cont.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "finish"))
) #find or locate the class before excuting the next code

finish = driver.find_element(By.ID, "finish")
finish.click()

input("Press enter to close...")
driver.quit()

"""
Bug 1 encoutered: You cannot press enter when submitting information on checking out the items,
 you need to fill up first all the info before hitting enter.

 -You cannot pass through when you don't fill out the information
"""



