import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

standard_user = 'standard_user'
locked_out_user = 'locked_out_user'
PASSWORD = 'secret_sauce'
LOGIN = 'login-button'

'''For Chrome'''
driver = webdriver.Chrome(
    executable_path='C:\\Users\Дима\\PycharmProjects\\Course Python and Selenium\\Automation-and-Programming-by-Python-and-Selenium\\python_selenium\\chromedriver.exe')
'''For Firefox'''
# options = Options()
# options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
# driver = webdriver.Firefox(options=options)

driver.get('https://www.saucedemo.com/')
"""Открывает полноэкранный режим"""
driver.maximize_window()
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys('standard_user')
enter_password = driver.find_element(By.ID, 'password')
enter_password.send_keys('secret_sauce')
login = driver.find_element(By.ID, 'login-button').click()
# time.sleep(2)
# driver.close()
