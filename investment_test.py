import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class EFSTest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_efs(self):
           user = "instructor"
           pwd = "instructor1a"
           driver = self.driver
           driver.maximize_window()
           driver.get("https://stuti-eaglefinanceproject.herokuapp.com")#directs to website
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/p[2]/a").click()
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(1)

           # click add investment button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
           time.sleep(2)
           elem = driver.find_element_by_xpath('//*[@id="id_customer"]').click()
           select = Select(driver.find_element_by_xpath('//*[@id="id_customer"]'))
           time.sleep(0)
           elem = select.select_by_index("1")  # choose customer id 1
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_category"]')
           elem.send_keys("property")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_description"]')
           elem.send_keys("401K with UNO")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_acquired_value"]')
           elem.send_keys("3000")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_recent_value"]')
           elem.send_keys("4000")
           time.sleep(0)
           #click save
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
           time.sleep(2)

           # Edit Investment
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[7]/td[8]/a").click()
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_description"]')  # edited the description field
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("402 Mutual of Omaha")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_acquired_value"]')  # edited the acquired value field
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("5000")
           time.sleep(0)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()  # click update button

           # Click the delete button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[8]/td[9]/a").click()
           time.sleep(1)
           elem = driver.switch_to.alert.accept()  # Accepts to delete the field
           time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()
