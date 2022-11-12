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

"""INFO Product #1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print('Name Product #1 is:', value_product_1)
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print('Price Product #1 is:', value_price_product_1)
select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print('Enter Cart')


"""INFO Cart Product #1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
cart_value_product_1 = cart_product_1.text
print('Name Product #1 in Cart is:', cart_value_product_1)
assert value_product_1 == cart_value_product_1
print('Name Product #1 in Cart is: GOOD')

cart_price_product_1 = driver.find_element(By.XPATH,
                                           "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
cart_value_price_product_1 = cart_price_product_1.text
print('Price Product #1 in Cart is:', cart_value_price_product_1)
assert value_price_product_1 == cart_value_price_product_1
print('Price Product #1 in Cart is: GOOD')

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print('Click Checkout')

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Dima')
print('Input First Name')
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Chernukho')
print('Input Last name')
postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('220100')
print('Input Postal Code')
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print('Click Continue')

"""INFO Finish Product #1"""
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
finish_value_product_1 = finish_product_1.text
print('Name Product #1 in Finish is:', finish_value_product_1)
assert value_product_1 == finish_value_product_1
print('Name Product #1 in Finish is: GOOD')

finish_price_product_1 = driver.find_element(By.XPATH,
                                             "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
finish_value_price_product_1 = finish_price_product_1.text
print('Price Product #1 in Finish is:', finish_value_price_product_1)
assert value_price_product_1 == finish_value_price_product_1
print('Price Product #1 in Finish is: GOOD')

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = 'Item total: ' + finish_value_price_product_1
print(item_total)
assert value_summary_price == item_total
print('Total Summary Price is GOOD')
sum_product_1 = finish_value_price_product_1
print(float(sum_product_1[1:]))




time.sleep(2)

driver.close()
