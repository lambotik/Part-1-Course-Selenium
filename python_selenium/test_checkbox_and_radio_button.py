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

base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()
checkbox_1 = driver.find_element(By.XPATH, "//input[@value='cb1']")
time.sleep(2)
checkbox_1.click()
print('Click Checkbox 1')
checkbox_3 = driver.find_element(By.XPATH, "//input[@value='cb3']")
time.sleep(2)
checkbox_3.click()
print('Click Checkbox 3')

radio_button_1 = driver.find_element(By.XPATH, "//input[@value='rd1']")
radio_button_1.click()
time.sleep(2)
print('Click RadioButton 1')

driver.close()
