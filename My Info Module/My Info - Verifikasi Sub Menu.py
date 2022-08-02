from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#My Info - Verifikasi sub-menu yang ada di dalam tab My Info
#1) Buka browser Chrome
#2) Akses URL https://opensource-demo.orangehrmlive.com/
#3) Input username (Admin)
#4) Input password (admin123)
#5) Login
#6) Masuk halaman My Info
#7) Verifikasi sub-sub menu
#8) Close browser

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

elem = driver.find_element(By.NAME, 'txtUsername')
elem.clear()
elem.send_keys("Admin")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, 'txtPassword')
elem.clear()
elem.send_keys("admin123")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, 'menu_pim_viewMyDetails')
elem.click()

#verify Contact Details
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[2]/a')
elem.click()

#verify Emergency Contacts
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[3]/a')
elem.click()

#verify Dependents
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[4]/a')
elem.click()

#verify Immigration
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[5]/a')
elem.click()

#verify Job
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[6]/a')
elem.click()

#verify Salary
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[7]/a')
elem.click()

#verify Tax Exemptions
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[8]/a')
elem.click()

#verify Report-to
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[9]/a')
elem.click()

#verify Qualifications
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[10]/a')
elem.click()

#verify Memberships
elem = driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[11]/a')
elem.click()

driver.close()

print('***All Sub-menus Successfully Loaded***')
print('***Test Passed***')