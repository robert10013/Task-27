import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_input_locator = (By.NAME, "username")
        self.password_input_locator = (By.NAME, "password")
        self.login_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        self.dashboard_locator = (By.CSS_SELECTOR, "div.oxd-topbar-header-breadcrumb > h6")

        def open(self):
            self.driver.get(self.url)

            def enter_username(self, username):
                username_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.username_input_locator)
                )
                username_input.send_keys(username)

                def enter_password(self, password):
                    password_input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(self.password_input_locator)
                    )
                    password_input.send_keys(password)

                    def click_login(self):
                        login_button = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located(self.login_button_locator)
                        )
                        login_button.click()

                        def is_login_successful(self):
                            return WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located(self.dashboard_locator)
                            )
                        def get_test_data():
                            df = pd.read_excel('test_data.xlsx')
                            return df.to_dict(orient='records')
                        @pytest.fixture
                        def driver( ):
                            driver = webdriver.chrome()
                            yield driver
                            driver.quiet()
                            @pytest.mark.parametrize("test_data",get_test_data())
                            def test_login(driver,test_data):
                                login_page=LoginPage(driver)


                                login_page.open()


                                login_page.enter_username(test_data['username'])
                                login_page.enter_password(test_data['password'])


                                login_page.click_login()


                                try:
                                    login_successful=login_page.is_login_successful()
                                    if login_successful:
                                        test_data['Test Result']='Passed'
                                    else:
                                        test_data['Test Result']='Failed'
                                except Exception as e:
                                    test_data['Test Result']='Failed'


                                    test_data['Date']=datetime.now().strftime('%Y-%m-%d')
                                    test_data['Time of Test']=datetime.now().strftime('%H:%M:%S')


                                    test_data['Name of Tester']='Automated tester'

                                    df=pd.DataFrame(get_test_data())
                                    df.to_excel('test_data.xlsx', index=False)














