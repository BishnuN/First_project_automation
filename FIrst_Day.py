import time
from selenium import webdriver
print("\t\t****Select driver you want to use****\n")
print("\t\t1-> Chrome\n\t\t2-> Firefox\n\t\tany number->Microsoft Edge")
num = input("\tEnter Number:")
num = int(num)
if num == 1:
    driver = webdriver.Chrome()
    time.sleep(10)
elif num == 2:
    driver = webdriver.Firefox()
    time.sleep(10)
else:
    driver = webdriver.Edge()
    time.sleep(10)