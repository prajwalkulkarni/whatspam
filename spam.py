from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys




class Spam:

    def __init__(self,usr,msg,count):
        self.usr = usr
        self.msg = msg
        self.count = count
        self.retry = 0
        self.complete = False

    def startspam(self):
        int(input()) #intermediate input key to proceed execution
        #search=driver.find_element_by_name("gQzdc")
        #search.send_keys("{}".format(self.usr)+Keys.RETURN)

        try:
            user = driver.find_element_by_xpath("//span[@title='{}']".format(self.usr))
            user.click()
            text= driver.find_element_by_class_name('_1Plpp')

            for i in range(count):
                text.send_keys("{}".format(msg)+Keys.RETURN)

            self.complete = True
                
        except NoSuchElementException:
            print("No contact/group found,Try with other name")
            self.complete = False

        finally:
            dict = {True:"Spamming completed,try again? 1:yes ,2:exit",False:"Spam unsuccessful,try again? 1:yes, 2:exit"}
            print(dict[self.complete])

            retry = int(input())

            if retry == 1:
                self.usr = input("Enter receipient/group name:")
                self.msg = input("Enter spam message:") #Message body
                self.count = int(input("Enter count:"))
                startspam(self)

            elif retry == 2:
                sys.exit()

            else:
                print("Invalid input")
                sys.exit()
            
       

    

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    assert "WhatsApp" in driver.title
    usr = input("Enter recipient/group Name:")
    msg = input("Enter spam message:") #Message body
    count = int(input("Enter count:"))

    spam = Spam(usr,msg,count)
    spam.startspam()



