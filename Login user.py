import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qaecoma.bishalkarki.xyz/index.php")
time.sleep(3)
nav_driver = driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
nav_driver.click()
time.sleep(3)
email = driver.find_element(By.ID,"email")
time.sleep(5)
email.send_keys("hello@gmail.com")
time.sleep(5)
password = driver.find_element(By.ID,"passwd")
password.send_keys("hello@gmail.com")
time.sleep(3)
login = driver.find_element(By.ID,"SubmitLogin")
login.click()
time.sleep(3)


