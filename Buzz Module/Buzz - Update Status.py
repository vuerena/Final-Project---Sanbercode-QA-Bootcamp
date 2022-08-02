from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#Buzz - Update Status
#1) Buka browser Chrome
#2) Akses URL https://opensource-demo.orangehrmlive.com/
#3) Input username (Admin)
#4) Input password (admin123)
#5) Login
#6) Masuk halaman Buzz
#7) Input text status
#8) Klik Post
#9) Verifikasi apakah postingan berhasil ditampilkan
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

elem = driver.find_element(By.ID, 'menu_buzz_viewBuzz')
elem.click()

elem = driver.find_element(By.ID, 'createPost_content')
elem.clear()
elem.send_keys("Ini adalah sebuah status.")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, 'postSubmitBtn')
elem.click()


search_elem = driver.find_element(By.ID, 'postBody')
search_elem = search_elem.is_displayed()
if search_elem == True:
    print("***Update Status Test Passed***")
else:
    print("Failed")

driver.close()
