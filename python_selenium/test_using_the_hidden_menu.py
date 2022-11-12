import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

standard_user = 'standard_user'
locked_out_user = 'locked_out_user'
PASSWORD = 'secret_sauce'
LOGIN = 'login-button'

'''For Chrome'''
driver = webdriver.Chrome(
    executable_path='C:\\Users\Дима\\PycharmProjects\\Course Python and Selenium\\Automation-and-Programming-by-Python-and-Selenium\\python_selenium\\chromedriver.exe')

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys(standard_user)
print('\nInput login user')
enter_password = driver.find_element(By.ID, 'password')
enter_password.send_keys(PASSWORD)
print('Input password')
login = driver.find_element(By.ID, 'login-button').click()
print('Click button login')
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
print('Click burger menu')
time.sleep(2)
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']").click()

driver.close()
