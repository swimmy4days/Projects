from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://youtube.com")
search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys('captainsparklez')
search = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search.click()
