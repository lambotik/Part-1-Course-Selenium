import datetime
import time
from selenium import webdriver
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
"""Создаем переменную которая записывает дату и время"""
now_date = datetime.datetime.utcnow().strftime(' %d.%m.%Y %H.%M.%S')
"""Создаем переменную screenshot к которой добавляем now_date(так мы получаем уникальное значение имени скриншота). Можно в название скриншота указывать имя конкретного теста к которому он относится"""
name_screenshot = 'screenshot' + now_date + '.png'
"""Делаем полноэкранный режим"""
driver.maximize_window()
"""Выставляем явное ожидание, чтобы страница успела загрузится"""
time.sleep(5)
"""Сохраняем скриншоты в отдельную директорию"""
driver.save_screenshot(
    'C:\\Users\Дима\\PycharmProjects\\Course Python and Selenium\\Automation-and-Programming-by-Python-and-Selenium\\python_selenium\\screen\\' + name_screenshot)

time.sleep(2)
driver.close()
