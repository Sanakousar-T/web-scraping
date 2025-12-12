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
iphone_data = driver.find_elements("xpath","//div[@class='KzDlHZ']")
d = {}
for i in iphone_data:
    data = i.text
    if data[-7:-1] not in d:
        d[data[-7:-1]] = [data]
    else:
        d[data[-7:-1]] += [data]
print(d)
print("Data Extrcated Successfully")
driver.close()