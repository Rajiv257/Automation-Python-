from selenium import webdriver
import pyautogui as pg
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
url = 'http://www.becbapatla.ac.in:8080/STUDENTINFO/index.html'
regd = 'Y17ACS'
no = 480
driver.get(url)

for i in range(1, 175):
    no = no + 1
    regd = regd[0:6] + no.__str__()
    driver.find_element_by_name("id").clear()
    driver.find_element_by_name("id").send_keys(regd)
    pg.hotkey('enter')
    try:
        if driver.find_element_by_xpath("/html/body/div/div/div[5]/div/div/div/table[1]/tbody/tr[2]/td").text == "MADDINENI RAJIV GANDHI" or driver.find_element_by_xpath("/html/body/div/div/div[5]/div/div/div/center/strong/font").text == "Incorrect Registered Number.":
            driver.fullscreen_window()
            break
    except NoSuchElementException:
        driver.back()
    else:
        driver.back()
else:
    print("No Record Found")