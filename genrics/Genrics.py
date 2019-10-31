from selenium.webdriver.common.by import By
import logging

class Genrics:
    def __init__(self,driver):
        self.driver=driver

    logging.basicConfig(filename='testlog', level=logging.INFO,
                        format="%(asctime)s: %(levelname)s: %(message)s")

    def getByType(self,locatortype):
        locator=locatortype.lower()
        if locator=='id':
            return By.ID
        elif locator=='name':
            return By.NAME
        elif locator=='class_name':
            return By.CLASS_NAME
        elif locator=='xpath':
            return By.XPATH
        elif locator=='tagname':
            return By.TAG_NAME
        elif locator=='linkpartialtext':
            return By.LINK_TEXT
        else:
            logging.info(('locator ',locatortype,' is not found'))
        return False

    def getElement(self,locatortype,locatorvalue):
        try:
            bytype=self.getByType(locatortype)
            element=self.driver.find_element(bytype,locatorvalue)
            logging.info(('element with locator type ',locatortype,' and locator value ',
                  locatorvalue,'is found'))
        except:
            print('element with locator type ', locatortype, ' and locator value ',
                  locatorvalue, 'is not found')
        return element

    def sendData(self,locatortype,locatorvalue,data):
        try:
            getelement=self.getElement(locatortype,locatorvalue)
            getelement.send_keys(data)
            logging.info(('data ',data,' sent to the element with locator type ',
                  locatortype,' with locator value ',locatorvalue))
        except:
            print('data ', data, ' is not sent to the element with locator type ',
                  locatortype, ' with locator value ',locatorvalue)

    def clickOn(self,locatortype,locatorvalue):
        try:
            getelement=self.getElement(locatortype,locatorvalue)
            getelement.click()
            logging.info(('clicked on a element with locator type ',locatortype,' and locator value ',
                  locatorvalue))
        except:
            print('cannot click on a element with locator type ', locatortype,
                  ' and locator value ', locatorvalue)

