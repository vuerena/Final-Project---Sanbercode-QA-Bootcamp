from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#Directory - Search Directory
#1) Buka browser Chrome
#2) Akses URL https://opensource-demo.orangehrmlive.com/
#3) Input username (Admin)
#4) Input password (admin123)
#5) Login
#6) Masuk halaman Directory
#7) Input nama yang akan dicari (Cecil Bonaparte)
#8) Klik Search
#9) Verifikasi apakah tabel hasil pencarian ditampilkan
#10) Close browser

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

elem = driver.find_element(By.ID, 'menu_directory_viewDirectory')
elem.click()

elem = driver.find_element(By.NAME, 'searchDirectory[emp_name][empName]')
elem.clear()
elem.send_keys("Cecil Bonaparte")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, 'searchBtn')
elem.click()

search_elem = driver.find_element(By.ID, 'searchResults')
search_elem = search_elem.is_displayed()
if search_elem == True:
    print("***Test Passed***")
else:
    print("Failed")

driver.close()
