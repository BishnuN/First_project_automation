import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qaecoma.bishalkarki.xyz/index.php")

    def tearDown(self):
        self.driver.close()


    def test_something(self):
        driver = self.driver
        try:
                nav_signin = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
                nav_signin.click()

                emailfirst = driver.find_element(By.ID, 'email_create')
                emailfirst.send_keys("jitesh@gmail.com")

                createaccount = driver.find_element(By.ID, 'SubmitCreate')
                createaccount.click()
                driver.implicitly_wait(10)

                firstname = driver.find_element(By.ID, 'customer_firstname')
                firstname.send_keys("Jitesh")
                time.sleep(2)

                lastname = driver.find_element(By.ID, 'customer_lastname')
                lastname.send_keys("Thapa")
                time.sleep(2)

                email = driver.find_element(By.ID, 'email')
                email.clear()
                email.send_keys("jitesh@gmail.com")
                time.sleep(2)

                password = driver.find_element(By.ID, 'passwd')
                password.send_keys("hello123")
                time.sleep(2)

                button_register = driver.find_element(By.ID, 'submitAccount')
                button_register.click()
                time.sleep(2)

        except Exception as e:
            print(e)

        expected_result = "Jitesh Thapa"
        actual_result = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text
        self.assertEqual(expected_result, actual_result, "Registration unsuccessful")




if __name__ == '__main__':
    unittest.main()

