from time import sleep
from genrics.Genrics import Genrics
#from base.genrics import Genrics
from genrics.genricscreenshot import getScreenShot

class LoginPage(Genrics):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    usn_text_field='identifierId'
    next_button="//div[@class='ZFr60d CeoRYc']"
    pw_text_filed="password"
    next_button1 = "//div[@class='ZFr60d CeoRYc']"
    profile_text="//span[@class='gb_xa gbii']"
    signout_button="//a[text()='Sign out']"

 # ************************************************************************
    def enterUsername(self,username):
        #self.getUsernameTextField().send_keys(username)
        self.sendData('id',self.usn_text_field,username)

    def clickNext(self):
        #self.getUsernameTextField().send_keys(username)
        self.clickOn('xpath',self.next_button)

    def enterPassword(self,password):
        #self.getPasswordTextField().send_keys(password)
        self.sendData('name',self.pw_text_filed,password)

    def clickNext1(self):
        #self.getUsernameTextField().send_keys(username)
        self.clickOn('xpath',self.next_button1)

    def profilePic(self):
        # self.getUsernameTextField().send_keys(username)
        self.clickOn('xpath', self.profile_text)

    def clickSigninButton(self):
       # self.getLoginButton().click()
        self.clickOn('id',self.signout_button)

# ************************************************************************

    def loginTest(self,usn,nxt,pwd,nxt1):
        self.enterUsername(usn)
        self.clickNext()
        self.enterPassword(pwd)
        self.clickNext1()
        self.profilePic()
        self.clickSigninButton()

    def verifyLogin(self):
        expected_title='Inbox - connect.skybet1@gmail.com - Gmail'
        sleep(3)
        actual_title=self.driver.title
        if expected_title != actual_title:
            getScreenShot(self.driver)
            assert expected_title==actual_title



 #************************************************************************
    '''def getUsernameTextField(self):
        return self.driver.find_element_by_id(self.usn_text_field)
    def getPasswordTextField(self):
        return self.driver.find_element_by_name(self.pwd_text_field)
    def getLoginButton(self):
        return self.driver.find_element_by_id(self.login_button)'''