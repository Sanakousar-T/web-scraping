from selenium.webdriver import Chrome, ChromeOptions
from time import sleep


opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = Chrome(options=opts)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
search = driver.find_element("name", "q")
search.send_keys("iphone")
sleep(2)
search.submit()
sleep(3)
data = driver.find_elements("xpath", "//div[@class='KzDlHZ']")
iphone = []
for i in data:
    iphone.append(i.text)
print(iphone)
path = r"D:\Qspider\python selenium marathahalli\web scraping\iphone"
with open(path, "w") as file:
    for i in iphone:
        file.write(f"{i}\n")
driver.close()