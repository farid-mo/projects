# -*- coding: utf-8 -*-
"""
Automation with selenium.
Demo: https://demo.seleniumeasy.com/

Selenium cheat sheet:
    http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
Created on Thu Feb 3 2022

@author: Farid
"""
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

# Maximize window
chrome_browser.maximize_window()

# Go to the url
url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'
chrome_browser.get(url)

# Check if an element is exist
assert 'Selenium Easy Demo' in chrome_browser.title

# Check for 'show message' button
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

# Check show message button in page source
assert 'Show Message' in chrome_browser.page_source

# Grab the input box
user_message = chrome_browser.find_element_by_id('user-message')
# Clear the box
user_message.clear()
# Send string
user_message.send_keys('I am cool!')
# Simulate a click
show_message_button.click()
# Find the output message
output_message = chrome_browser.find_element_by_id('display')
assert 'I am cool!' in output_message.text

# Close the browser
# Option one: close x 2 > maybe the first one does not get the job done.
chrome_browser.close()
chrome_browser.close()

# Option two: quit -> closes all sessions
chrome_browser.quit()
