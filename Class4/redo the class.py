# from selenium import webdriver
# driver = webdriver.Firefox(executable_path= "/Users/yonimac/Downloads/geckodriver")
# driver.get("https://walla.co.il")
#
#
# title = driver.walla.co.il
# # driver.refresh()
# # if title==driver.title:
# #     print("equal")
# #
#
# # from selenium import webdriver
# # driver = webdriver.Chrome(executable_path="/Users/yonimac/Downloads/Chromedriver")
# #
# # driver.get("https://www.google.com")
#
# from selenium import webdriver
# import time
#
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
# driver = webdriver.Chrome(chrome_options=options)
# driver.get("https://buyme.co.il")
#
# # click radio button
# python_button = driver.find_elements_by_xpath('//*[@id="ember589"]/div/ul[1]/li[3]/a/span[1]')[0]
# python_button.click()
# #
# # # type text
# # text_area = driver.find_element_by_id('textarea')
# # text_area.send_keys("print('Hello World')")
# #
# # # click submit button
# # submit_button = driver.find_elements_by_xpath(
# #     '//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
# # submit_button.click()

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="/Users/yonimac/Downloads/chromedriver")
driver.get("https://buyme.co.il")
# click radio button
python_button = driver.find_elements_by_xpath('//div[@id="ember589"]/div/ul[1]/li[3]/a/span[1]')[0]
python_button.click()
# type user and password
elem = driver.find_element_by_id("ember997")
elem.send_keys("yavyrach@gmail.com")
element = driver.find_element_by_id("ember999")
element.send_keys('#Yav2012')

driver.find_element_by_xpath('//*[@id="ember989"]/button').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="ember662_chosen"]/a').click()
driver.find_element_by_xpath('//*[@id="ember662_chosen"]/div/ul/li[3]').click()