import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qaecoma.bishalkarki.xyz/admin123/index.php?")

    def tearDown(self):
        self.driver.close()


    def test_something(self):
        driver = self.driver
        try:
                super_email = driver.find_element(By.ID, 'email')
                super_email.send_keys("admin@qaecoma.bishalkarki.xyz")

                super_pass = driver.find_element(By.ID, 'passwd')
                super_pass.send_keys("Test123!@#")

                super_login = driver.find_element(By.XPATH, '//*[@id="login_form"]/div[3]/button')
                super_login.click()
                time.sleep(2)

                adminstration = driver.find_element(By.XPATH, '//*[@id="maintab-AdminAdmin"]/a')
                actions = ActionChains(driver)
                actions.move_to_element(adminstration).perform()
                time.sleep(2)

                employee = driver.find_element(By.XPATH, '//*[@id="subtab-AdminEmployees"]/a')
                employee.click()
                time.sleep(2)

                add_employee = driver.find_element(By.ID, 'page-header-desc-employee-new_employee')
                add_employee.click()
                time.sleep(2)


                firstname = driver.find_element(By.ID, 'firstname')
                firstname.send_keys("Govinda")
                time.sleep(2)

                lastname = driver.find_element(By.ID, 'lastname')
                lastname.send_keys("Basnet")
                time.sleep(2)

                email = driver.find_element(By.ID, 'email')
                email.clear()
                email.send_keys("gopal@gmail.com")
                time.sleep(2)

                password = driver.find_element(By.ID, 'passwd')
                password.send_keys("hello123")
                time.sleep(2)

                role_assign = driver.find_element(By.ID, 'id_profile')
                select_role = Select(role_assign)
                select_role.select_by_visible_text("Logistician")

                activation = driver.find_element(By.ID, 'active_on')
                if not activation.is_selected():
                    activation.click()

                save = driver.find_element(By.XPATH, '//*[@id="employee_form_submit_btn"]/i')
                save.click()
                time.sleep(2)

        except Exception as e:
            print(e)


        expected_result = "5"
        actual_result = driver.find_element(By.XPATH, '//*[@id="form-employee"]/div/div[1]/span[1]').text


        self.assertEqual(expected_result, actual_result, "Registration unsuccessful")
        #self.assertEqual(expected_result2, actual_result2, "Registration unsuccessful")



if __name__ == '__main__':
    unittest.main()


