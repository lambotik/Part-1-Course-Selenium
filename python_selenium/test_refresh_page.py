import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_wrong_user_name():
    standard_user = 'standard_use'
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
    enter_password = driver.find_element(By.ID, 'password')
    enter_password.send_keys(PASSWORD)
    print('Input password')
    login = driver.find_element(By.ID, 'login-button').click()
    print('Click button login')
    warrning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    value_warrning_text = warrning_text.text
    print(value_warrning_text)
    assert value_warrning_text == 'Epic sadface: Username and password do not match any user in this service'
    print('Wrong user name')
    '''Обновление страницы'''
    driver.refresh()
    time.sleep(2)
    driver.close()



