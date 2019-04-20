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
           #Clicks stock view details
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[3]/div/div/p[2]/a").click()
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(1)

           # click add stock button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
           time.sleep(2)
           elem = driver.find_element_by_xpath('//*[@id="id_customer"]').click()
           select = Select(driver.find_element_by_xpath('//*[@id="id_customer"]'))
           time.sleep(0)
           elem = select.select_by_index("1")  # choose customer id 1
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_symbol"]')
           elem.send_keys("googl")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_name"]')
           elem.send_keys("Google new")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_shares"]')
           elem.send_keys("5000")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_purchase_price"]')
           elem.send_keys("100")
           time.sleep(0)
           # click save
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
           time.sleep(2)

           # Edit Stock
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[7]/a").click()
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_purchase_price"]')  # edited the purchase price field
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("100")
           time.sleep(1)
           elem = driver.find_element_by_xpath('//*[@id="id_purchase_date"]')  # edited the purchase date
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("2012-06-06")
           time.sleep(2)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()  # click update button
           time.sleep(2)

           #Click the delete button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[5]/td[8]/a").click()
           time.sleep(1)
           elem = driver.switch_to.alert.accept()  # Accepts to delete the field
           time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()
