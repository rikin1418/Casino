from selenium import webdriver
from time import sleep
from pages.loginpage import LoginPage
import pytest
import unittest
from genrics import genricsxl

@pytest.mark.usefixtures('prePostMethod')
class TestDemo(unittest.TestCase):
    file_path="C:\\Users\\ukumar\\Desktop\\casinotestdata.xlsx"
    pagename="Sheet1"

    @pytest.fixture(autouse=True)
    def classObj(self,prePostMethod):
        # create object for LopginPage class
        self.lp = LoginPage(self.driver)

    def testValidLogin(self):
        username=genricsxl.readData(self.file_path,self.pagename,0,0)
        password=genricsxl.readData(self.file_path,self.pagename,0,1)
        self.lp.loginTest(username,password)
        self.lp.clickNext()
        self.lp.clickNext1()
        self.lp.profilePic()
        self.lp.clickSigninButton()
        self.lp.verifyLogin()
        sleep(3)

    def testInvalidLogin(self):
        username = genricsxl.readData(self.file_path, self.pagename, 1, 0)
        password = genricsxl.readData(self.file_path, self.pagename, 1, 1)
        self.lp.loginTest(username,password)
        self.lp.verifyLogin()
        sleep(3)

