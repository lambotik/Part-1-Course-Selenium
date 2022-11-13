import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

'''For Chrome'''
driver = webdriver.Chrome(
    executable_path='C:\\Users\Дима\\PycharmProjects\\Course Python and Selenium\\Automation-and-Programming-by-Python-and-Selenium\\python_selenium\\chromedriver.exe')

base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()
action = ActionChains(driver)
square_slider = driver.find_element(By.XPATH, "//input[@class='slider-square']")
"""click_and_hold - нажимает и удерживает, move_by_offset(100, 0) - первое значение(перемещение по горизонтали),
 второе значение(перемещение по вертикали),release() - отпустить ползунок, perform() - сохраняет результат"""
action.click_and_hold(square_slider).move_by_offset(100, 0).release().perform()

time.sleep(4)
driver.close()
