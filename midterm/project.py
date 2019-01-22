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
# Drop Down
sleep(2)
driver.find_element_by_xpath('//*[@id="ember662_chosen"]/a').click()
driver.find_element_by_xpath('//*[@id="ember662_chosen"]/div/ul/li[3]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="ember677_chosen"]/a').click()
driver.find_element_by_xpath('//*[@id="ember677_chosen"]/div/ul/li[2]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="ember686_chosen"]/a').click()
driver.find_element_by_xpath('//*[@id="ember686_chosen"]/div/ul/li[7]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="ember721"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="ember1141"]/div/div[1]/img').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="ember1231"]/span').click()
sleep(2)
#Text and Email
elem = driver.find_element_by_id("ember1310")
elem.send_keys("Aviel")
#Drop down
driver.find_element_by_xpath('//*[@id="ember1314_chosen"]/a/span').click()
driver.find_element_by_xpath('//*[@id="ember1314_chosen"]/div/ul/li[3]').click()
sleep(2)
elem = driver.find_element_by_id('ember1337')
elem.send_keys('/Users/yonimac/Documents/devops.png')
#email and sumbit
driver.find_element_by_xpath('//*[@id="ember1276"]/div[4]/div/div[1]/div[2]/div/button/span/span[1]').click()
sleep(2)
elem = driver.find_element_by_id('ember1772')
elem.send_keys("yrachmani@gmail.com")
sleep(2)
driver.find_element_by_xpath('//*[@id="ember1276"]/div[4]/div/div[3]/div/div[2]/button[2]').click()
driver.find_element_by_xpath('//*[@id="ember1276"]/div[5]/button').click()
sleep(2)
#pay and go
driver.find_element_by_xpath('//*[@id="ember1808"]/div[5]/button').click()
driver.close()

