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

base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()
action = ActionChains(driver)
double_click = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click).perform()
response_double_click = driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']")
value_response_double_click = response_double_click.text
print(value_response_double_click)
assert value_response_double_click == 'You have done a double click'
print('Double click done')

right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click).perform()
response_right_click = driver.find_element(By.XPATH, "//p[@id='rightClickMessage']")
value_response_right_click = response_right_click.text
print(value_response_right_click)
assert value_response_right_click == 'You have done a right click'
print('Right click done')

time.sleep(2)
driver.close()
