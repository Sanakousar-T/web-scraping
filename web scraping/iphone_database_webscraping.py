from selenium.webdriver import Chrome, ChromeOptions
from time import sleep


opts = ChromeOptions()
opts.add_experimental_option("detach", True)

import sqlite3
conn = sqlite3.connect("iphone_data.db")
cursor = conn.cursor()
#cursor.execute("create table iphone(name varchar(200), price varchar(32));")

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

for i, j in zip(iphone_data, price_data):
    cursor.execute(f"insert into iphone values('{i.text}','{j.text}');")
    conn.commit()
print("data saved successfully..")
sleep(3)
driver.close()






