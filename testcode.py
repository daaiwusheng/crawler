from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(900, 800))
display.start()

driver = webdriver.Chrome()
driver.get('https://blog.csdn.net/Lyn_B/article/details/107461556')
print(driver.title)

driver.quit()
display.stop()