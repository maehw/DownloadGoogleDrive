# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile = webdriver.FirefoxProfile()

profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '<destination-folder>')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('image/jpeg'))


driver = webdriver.Firefox(profile)

#driver.get('https://drive.google.com/drive/folders/<your-shared-folder>')

time.sleep(5)
driver.find_element_by_tag_name('body').send_keys('v') 

# skip some photos
for x in range(0, 1749):
	driver.find_element_by_tag_name('body').send_keys(Keys.DOWN) 
	time.sleep(0.3)

driver.find_element_by_tag_name('body').send_keys(Keys.ENTER) 


download_count = 0
processing = True
while processing == True:
	time.sleep(3)

	try:
	    download_button = driver.find_element_by_xpath("//div[@data-tooltip='Herunterladen']")
	except NoSuchElementException:
	    print("Error: No download button found")
	    processing = False

	#print download_button

	#WebDriverWait(driver, 5).until(EC.element_to_be_clickable( download_button ));

	try:
	   download_button.click()
	   download_count += 1
	   print 'Download count: ', download_count 
	except Exception: 
	   print 'Failed to download (exception)'
	   pass
	


	time.sleep(2)

	try:
	    next_button = driver.find_element_by_xpath("//div[@data-tooltip='Weiter']")
	except NoSuchElementException:
	    print("Warning: No next button found - assuming 'finished' condition")
	    processing = False

	#print next_button
	next_button.click()
	
	
#browser.quit()

