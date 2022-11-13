import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

standard_user = 'standard_user'
locked_out_user = 'locked_out_user'
PASSWORD = 'secret_sauce'
LOGIN = 'login-button'

'''For Chrome'''
driver = webdriver.Chrome(
    executable_path='C:\\Users\Дима\\PycharmProjects\\Course Python and Selenium\\Automation-and-Programming-by-Python-and-Selenium\\python_selenium\\chromedriver.exe')

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()
"""Отработка исключения, если элемент не найден NoSuchElementException"""
try:
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
except NoSuchElementException as exception:
    print('NoSuchElementException')
    time.sleep(5)
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
    print('Click Visible Button')

driver.get('https://demoqa.com/radio-button')
yes_radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_radio_button.click()
"""Отработка исключения, если получено не верное ожидание AssertionError"""
try:
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == 'No'
except AssertionError as exception:
    driver.refresh()
    yes_radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radio_button.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == 'Yes'
    print('Radio Button Yes')
print('Test completed')

time.sleep(2)
driver.close()
