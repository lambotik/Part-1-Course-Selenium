import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


standard_user = 'standard_user'
PASSWORD = 'secret_sauce'

'''For Chrome'''
driver = webdriver.Chrome(
    executable_path='C:\\Users\Дима\\PycharmProjects\\Course Python and Selenium\\Automation-and-Programming-by-Python-and-Selenium\\python_selenium\\chromedriver.exe')

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys(standard_user)
print('\nInput login user')
# """Импортируем модуль Keys и стираем последние символы"""
# user_name.send_keys(Keys.BACKSPACE*3)
enter_password = driver.find_element(By.ID, 'password')
enter_password.send_keys(PASSWORD)
print('Input password')
"""Нажимаем кнопку ENTER пропуская её поиск"""
enter_password.send_keys(Keys.ENTER)

filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()
print('Click filter')
"""Имитируем одно нажатие стрелки вниз"""
filter.send_keys(Keys.DOWN)
time.sleep(2)
filter.send_keys(Keys.ENTER)

time.sleep(2)
driver.close()



