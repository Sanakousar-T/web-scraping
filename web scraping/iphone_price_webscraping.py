from selenium.webdriver import Chrome, ChromeOptions
from time import sleep


opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = Chrome(opts)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(3)
search = driver.find_element("name","q")
search.send_keys("Iphones")
sleep(2)
search.submit()
sleep(3)
iphone_data = driver.find_elements("xpath", "//div[@class='KzDlHZ']")
price_data = driver.find_elements("xpath", "//div[@class='Nx9bqj _4b5DiR']")
sleep(3)
path = r"D:\Qspider\python selenium marathahalli\web scraping\iphone_price"
with open(path, "a") as file:
    for i, j in zip(iphone_data, price_data):
        file.write(f"{i.text},{j.text}\n")

driver.close()



