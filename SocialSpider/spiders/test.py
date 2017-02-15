from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1024, 768))
display.start()

driver= webdriver.Firefox()
driver.get("http://weixin.sogou.com/weixin?type=1&query=newsbro")
#x = "//li[contains(@id,'sogou_vr_11002301_box_0')]"
x = "//a[contains(@uigs,'main_toweixin_account_image_0')]"
print 'driver.title, ',driver.title
url = driver.find_element_by_xpath(x).get_attribute("href")
print 'url, ',url
#driver.close() # Close the current window.
driver.quit() # Quit the driver and close every associated window.
display.stop()

