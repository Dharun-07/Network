from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('http://www.skillrack.com/faces/ui/profile.xhtml')
search=driver.find_element_by_xpath('//*[@id="input_j_id_s"]')
search.send_keys("")
passw=driver.find_element_by_xpath('//*[@id="input_j_id_u"]')
passw.send_keys("")
search.send_keys(Keys.ENTER)

