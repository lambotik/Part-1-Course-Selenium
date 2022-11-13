import datetime
import time
import until as until
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''For Chrome'''
driver = webdriver.Chrome(
    executable_path='C:\\Users\Дима\\PycharmProjects\\Course Python and Selenium\\Automation-and-Programming-by-Python-and-Selenium\\python_selenium\\chromedriver.exe')
start_test_time = datetime.datetime.now().strftime('%H:%M:%S')
print('Start Test Time: ', start_test_time)

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()
# driver.implicitly_wait(10)
# will_enable_button = driver.find_element(By.XPATH, "//button[@id='enableAfter']")
# will_enable_button.click()
will_enable_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='enableAfter']")))
will_enable_button.click()

end_test_time = datetime.datetime.now().strftime('%H:%M:%S')
print('Test End Time: ', end_test_time)

driver.close()
