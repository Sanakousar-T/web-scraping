from selenium.webdriver import Chrome, ChromeOptions
from time import sleep


opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = Chrome(options=opts)
driver.get("https://www.google.com/maps/")
driver.maximize_window()
driver.implicitly_wait(10)
search = driver.find_element("id", "searchboxinput")
search.send_keys("montissori schools in india")
driver.find_element("id", "searchbox-searchbutton").click()
scrollable_div = driver.find_element("class name", "e07Vkf.kA9KIf")

# Scroll down repeatedly until the end of the list is reached
while True:
    # Scroll to the bottom of the scrollable div
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
    sleep(2)

    # Check if "You've reached the end of the list." message is visible
    page_text = driver.find_element("tag name", 'body').text
    if "You've reached the end of the list." in page_text:
        print("Reached the end of the list.")
        break
search_list = driver.find_elements("xpath", "//a[@class='hfpxzc']")
for i in search_list:
    print(str(i.get_attribute('aria-label')))

driver.close()