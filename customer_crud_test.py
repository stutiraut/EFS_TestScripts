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
           driver.get("https://stuti-eaglefinanceproject.herokuapp.com/admin")#directs to website
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(1)
           elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a").click()
            #add new customer
           time.sleep(1)
           elem = driver.find_element_by_id("id_name")
           elem.send_keys("stuti")
           elem = driver.find_element_by_id("id_address")
           elem.send_keys("Uno")

           elem = driver.find_element_by_id("id_cust_number")
           elem.send_keys("50")

           elem = driver.find_element_by_id("id_city")
           elem.send_keys("Omaha")

           elem = driver.find_element_by_id("id_state")
           elem.send_keys("NE")

           elem = driver.find_element_by_id("id_zipcode")
           elem.send_keys("68106")

           elem = driver.find_element_by_id("id_email")
           elem.send_keys("sraut@unomaha.edu")

           elem = driver.find_element_by_id("id_cell_phone")
           elem.send_keys("1234888695")
           elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
           time.sleep(1)
           assert "Posted Blog Entry"
           elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[1]").click()
           time.sleep(1)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()#directs to customer detail
           time.sleep(1)

           #Clicks the edit button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[3]/td[9]/a").click()
           time.sleep(1)
           elem = driver.find_element_by_id("id_name")
           elem.send_keys(Keys.CONTROL + "a")
           elem.send_keys(Keys.DELETE)
           elem.send_keys("Stuti1")#Rename the name field
           time.sleep(2)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click() #Click update
           time.sleep(0)

           #Click the delete button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[5]/td[10]/a").click()
           time.sleep(2)
           elem = driver.switch_to.alert.accept() #Accepts to delete the field
           time.sleep(2)

           # Click the summary button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[11]/a").click()
           time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()


