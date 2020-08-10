from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")

input("press any key")

count = 1001

#a = driver.find_element_by_class_name("_3CneP")
#a = driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span")
a = driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[17]/div/div/div[2]/div[1]/div[1]/span")
a.click()

for i in range(0,count):
    b = driver.find_element_by_class_name("_3uMse")
    b.send_keys(f"hii {i}")
    c = driver.find_element_by_class_name("_1U1xa")
    c.click()



