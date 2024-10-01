import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qaecoma.bishalkarki.xyz/index.php")
driver.implicitly_wait(10)
nav_driver = driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
nav_driver.click()
driver.switch_to.alert()
email = driver.find_element(By.ID,"email")

email.send_keys("hello@gmail.com")

password = driver.find_element(By.ID,"passwd")
password.send_keys("hello@gmail.com")

login = driver.find_element(By.ID,"SubmitLogin")
login.click()



