import time
def getScreenShot(driver):
    path='C:\\Users\\ukumar\\PycharmProjects\\Casino\\screenshots\\'
    #path='D:\\demoproject\\screenshots\\'
    name=str(round(time.time()))+'.png'
    value=path+name
    driver.save_screenshot(value)