import unittest
from selenium import webdriver

class TestQuchemPediaSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_id(self):
        self.driver.get("localhost:8000/user/auth")
	## Email
        email = Select(self.driver.find_element_by_id('id_email'))
	email.send_keys("mohamed.ouhirragmail.com@")
	## PAssword
       	password1 = Select(self.driver.find_element_by_id('id_password1')
	password1.send_keys("123456789")
	password2 = Select(self.driver.find_element_by_id('id_password1')
	password2.send_keys("123456789")
	##Boutton submit
        btn = self.driver.find_element_by_css_selector("input[type=\"submit\"]")
        btn.click()
	## Verification
        page_url = self.driver.current_url
        msg_erreur = self.driver.find_element_by_class_name("errorlist")
	self.assertEqual(msg_erreur,'Enter a valid email address')

       
  
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
