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
print('Input login user')
enter_password = driver.find_element(By.ID, 'password')
enter_password.send_keys(PASSWORD)
print('Input password')
login = driver.find_element(By.ID, 'login-button').click()
print('Click button login')
# TEXT_PRODUCTS = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_products = TEXT_PRODUCTS.text
# print(value_text_products)
# assert value_text_products == 'PRODUCTS'
# print('GOOD')

url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
print(get_url)
assert url == get_url
print('GOOD URL')
driver.close()
