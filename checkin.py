#! usr/bin/python
# southwest airlines check in script

# imports
from selenium import webdriver
from selenium.webdriver import Safari
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# get user name and flight information 
first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
confirmation_num = input("Please enter your confirmation number: ")

# load the southwest webpage 
browser = webdriver.Safari()
browser.get('https://www.southwest.com/air/check-in/index.html')

# enter the values given 
browser.find_element_by_id('confirmationNumber').send_keys(confirmation_num)
browser.find_element_by_id('passengerFirstName').send_keys(first)
browser.find_element_by_id('passengerLastName').send_keys(last)

# submit the form
browser.find_element_by_id('form-mixin--submit-button').click()
