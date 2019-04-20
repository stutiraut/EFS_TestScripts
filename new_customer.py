import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

class EFSTest(unittest.TestCase):
   def setUp(self):
       self.driver = webdriver.Chrome()


   def test_efs(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://stuti-eaglefinanceproject.herokuapp.com/admin")  # directs to website
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a").click()
       time.sleep(1)
       data = open('customer.csv')
       datareader = csv.reader(data) #read data from csv file
       for row in datareader:
           if datareader.line_num == 1:
               continue
           else:
               name = row[0]
               address = row[1]
               custnum = row[2]
               city = row[3]
               state = row[4]
               zipcode = row[5]
               email = row[6]
               phone = row[7]
               time.sleep(1)

               elem = driver.find_element_by_id("id_name")
               elem.send_keys(name)
               time.sleep(0)
               elem = driver.find_element_by_id("id_address")
               elem.send_keys(address)
               time.sleep(0)
               elem = driver.find_element_by_id("id_cust_number")
               elem.send_keys(custnum)
               time.sleep(0)
               elem = driver.find_element_by_id("id_city")
               elem.send_keys(city)
               time.sleep(0)
               elem = driver.find_element_by_id("id_state")
               elem.send_keys(state)
               time.sleep(0)
               elem = driver.find_element_by_id("id_zipcode")
               elem.send_keys(zipcode)
               time.sleep(0)
               elem = driver.find_element_by_id("id_email")
               elem.send_keys(email)
               time.sleep(0)
               elem = driver.find_element_by_id("id_cell_phone")
               elem.send_keys(phone)
               time.sleep(0)
               elem.send_keys(Keys.RETURN)
               time.sleep(1)
               elem = driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
               time.sleep(1)
       driver.get("https://stuti-eaglefinanceproject.herokuapp.com")
       time.sleep(2)
       elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()  #
       time.sleep(1)

   def tearDown(self):
           self.driver.close()

if __name__ == "__main__":
    unittest.main()




