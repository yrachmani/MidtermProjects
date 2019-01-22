from selenium import webdriver
from time  import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome(executable_path= "/Users/yonimac/Downloads/chromedriver")
driver.get("https://buyme.co.il")
# click radio button
python_button = driver.find_elements_by_xpath('//div[@id="ember589"]/div/ul[1]/li[3]/a/span[1]')[0]
python_button.click()
# type user and password
elem = driver.find_element_by_id("ember997")
elem.send_keys("yavyrach@gmail.com")
wait: WebDriverWait = WebDriverWait(driver, 10)
element = driver.find_element_by_id("ember999")
element.send_keys('#Yav2012')
wait: WebDriverWait = WebDriverWaitebdr (driver,5)
driver.find_element_by_xpath('//*[@id="ember989"]/button').click()
# type Drop down
driver.find_element_by_xpath('//*[@id="ember989"]/button').click()
wait:(5)
driver.find_element_by_xpath('//*[@id="ember662_chosen"]/a').click()
driver.find_element_by_xpath('//*[@id="ember662_chosen"]/div/ul/li[3]'). click()
