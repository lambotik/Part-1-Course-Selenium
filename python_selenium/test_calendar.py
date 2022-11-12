import time
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

standard_user = 'standard_user'
locked_out_user = 'locked_out_user'
PASSWORD = 'secret_sauce'
LOGIN = 'login-button'

'''For Chrome'''
driver = webdriver.Chrome(
    executable_path='C:\\Users\Дима\\PycharmProjects\\Course Python and Selenium\\Automation-and-Programming-by-Python-and-Selenium\\python_selenium\\chromedriver.exe')

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()
new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
new_date.send_keys(Keys.BACKSPACE*10)
time.sleep(2)
now_date = datetime.datetime.utcnow().strftime('%m/%d/%Y')
print(now_date)
new_date.send_keys(now_date)
time.sleep(2)
"""Получаем завтрашний день"""
action = ActionChains(driver)
action.send_keys(Keys.DOWN).perform()
time.sleep(2)
action.send_keys(Keys.RIGHT).perform()
time.sleep(2)
action.send_keys(Keys.ENTER).perform()
time.sleep(2)
driver.close()
