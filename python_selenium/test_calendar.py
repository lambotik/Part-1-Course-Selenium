import time
import datetime

import item
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
driver.refresh()
new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
new_date.send_keys(Keys.BACKSPACE * 10)  # Очищаем поле ввода даты
time.sleep(1)
now_date = datetime.datetime.now().strftime('%m/%d/%Y')  # Получаем текущее значение даты в нужно формате
print('Выводим текущую дату: ', now_date)
new_date.send_keys(now_date)
time.sleep(1)
"""Получаем +10 дней от текущей даты"""
action = ActionChains(driver)
action.send_keys(Keys.DOWN).perform()  # активирует квадрат на текущей дате в календаре
time.sleep(1)
action.send_keys(Keys.RIGHT * 10).perform()  # перемещаем активированный квадрат на необходимое колл-во дней
time.sleep(1)
action.send_keys(Keys.ENTER).perform()  # выбираем полученную дату
time.sleep(1)
select_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
print('Выводим полученную дату(+10): ',
      select_date.get_attribute('value'))  # получаем значение введенное в строку ввода
now_server_date = datetime.datetime.utcnow().strftime('%m/%d/%Y %H.%M.%S')  # тут я так понял выводит время сервера
now_my_date = datetime.datetime.now().strftime('%m/%d/%Y %H.%M.%S')  # а тут время в моем часовом поясе
print('Время на сервере: ', now_server_date)
print('Мое текущее время: ', now_my_date)
driver.close()
