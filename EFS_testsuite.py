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
           time.sleep(0)
           elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a").click()
            #add new customer
           time.sleep(0)
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
           time.sleep(0)
           assert "Posted Blog Entry"
           elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[1]").click()
           time.sleep(0)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()#directs to customer detail
           time.sleep(0)

           #Clicks the edit button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[3]/td[9]/a").click()
           time.sleep(0)
           elem = driver.find_element_by_id("id_name")
           elem.send_keys(Keys.CONTROL + "a")
           elem.send_keys(Keys.DELETE)
           elem.send_keys("Stuts")#Rename the name field
           time.sleep(0)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click() #Click update
           time.sleep(0)

           #Click the delete button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[3]/td[10]/a").click()
           time.sleep(0)
           elem = driver.switch_to.alert.accept() #Accepts to delete the field
           time.sleep(0)
           # Click the summary button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[11]/a").click()
           time.sleep(0)

           #investment
           driver.get("https://stuti-eaglefinanceproject.herokuapp.com")
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/p[2]/a").click()

           # click add investment button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
           time.sleep(0)
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
           # click save
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
           time.sleep(0)

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
           time.sleep(1)

           #Stock
           driver.get("https://stuti-eaglefinanceproject.herokuapp.com")
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[3]/div/div/p[2]/a").click()
           # click add stock button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
           time.sleep(0)
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
           time.sleep(0)

           # Edit Stock
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[7]/a").click()
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_purchase_price"]')  # edited the purchase price field
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("100")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_purchase_date"]')  # edited the purchase date
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("2012-06-06")
           time.sleep(0)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()  # click update button
           time.sleep(0)

           # Click the delete button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a").click()
           time.sleep(0)
           elem = driver.switch_to.alert.accept()  # Accepts to delete the field
           time.sleep(0)
           # Bonds
           driver.get("https://stuti-eaglefinanceproject.herokuapp.com")
           # Clicks Bonds view details
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[4]/div/div/p[2]/a").click()
           time.sleep(0)
           # click add bonds button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
           time.sleep(2)
           elem = driver.find_element_by_xpath('//*[@id="id_customer"]').click()
           select = Select(driver.find_element_by_xpath('//*[@id="id_customer"]'))
           time.sleep(0)
           elem = select.select_by_index("2")  # choose customer id 1
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_symbol"]')
           elem.send_keys("test")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_name"]')
           elem.send_keys("Bond test")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_bonds"]')
           elem.send_keys("6000")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_purchase_price"]')
           elem.send_keys("200")
           time.sleep(0)
           # click save
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
           time.sleep(2)

           # Edit Bond
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[7]/a").click()
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_name"]')  # edited the name field
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("Selenium bond test")
           time.sleep(0)
           elem = driver.find_element_by_xpath('//*[@id="id_purchase_date"]')  # edited the purchase date
           elem.send_keys(Keys.CONTROL + 'a')
           elem.send_keys(Keys.DELETE)
           elem.send_keys("2014-12-06")
           time.sleep(0)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()  # click update button
           time.sleep(0)

           # Click the delete button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[3]/td[8]/a").click()
           time.sleep(1)
           elem = driver.switch_to.alert.accept()  # Accepts to delete the field
           time.sleep(0)



   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()


