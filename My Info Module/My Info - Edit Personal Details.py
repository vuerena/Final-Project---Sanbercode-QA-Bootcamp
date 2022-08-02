from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#My Info - Edit Personal Details
#1) Buka browser Chrome
#2) Akses URL https://opensource-demo.orangehrmlive.com/
#3) Input username (Admin)
#4) Input password (admin123)
#5) Login
#6) Masuk halaman My Info
#7) Edit Personal Info
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

elem = driver.find_element(By.ID, 'btnSave')
elem.click()

elem = driver.find_element(By.NAME, 'personal[txtEmpFirstName]')
elem.clear()
elem.send_keys("Bambang")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, 'personal[txtEmpMiddleName]')
elem.clear()
elem.send_keys("Putri")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, 'personal[txtEmpLastName]')
elem.clear()
elem.send_keys("Cantika")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, 'btnSave')
elem.click()

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title==expected_title:
    print("***Edit Personal Details Test Passed***")
else:
    print("Failed")

driver.close()
