from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import csv

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
chain = ActionChains(driver)
# example for naukri.com
driver.get('https://www.naukri.com/')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element("xpath", "//a[.='Login']").click()
driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("Enter your username")
driver.find_element("xpath", "//input[@type='password']").send_keys("Enter your password")
driver.find_element("xpath", "//button[text()='Login']").click()

driver.find_element("xpath", "//span[.='Search jobs here']").click()
driver.find_element("xpath", "(//input[@class='suggestor-input '])[1]").send_keys("QA ENGINEER")
driver.find_element("xpath", "(//input[@class='suggestor-input '])[2]").send_keys("Bengaluru")
driver.find_element("id", "jobType").click()

chain.move_to_element(driver.find_element("xpath", "//span[.='Job']")).click().perform()

driver.find_element("xpath", "//span[.='Search']").click()
sleep(3)
import csv

# Extract job cards
job_card = driver.find_elements("xpath", ".//div[contains(@class,'cust-job-tuple')]")

with open('naukri_jobs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['job_title', 'company_name', 'location', 'experience', 'salary', 'posted_date', 'job_summary', 'job_link',
         'skills'])

    for job in job_card:
        try:
            job_title = job.find_element("xpath", ".//a[contains(@class,'title')]").text
            company_name = job.find_element("xpath", ".//a[contains(@class,'comp-name')]").text
            location = job.find_element("xpath", ".//span[contains(@class,'locWdth')]").text
            experience = job.find_element("xpath", ".//span[contains(@class,'exp')]").text if job.find_elements("xpath",
            ".//span[contains(@class,'exp')]") else "NOT mentioned"
            salary = job.find_element("xpath", ".//span[contains(@class,'sal')]").text if job.find_elements("xpath",
             ".//span[contains(@class,'sal')]") else "NOT mentioned"

            try:
                posted_date = job.find_element("xpath", ".//span[contains(@class,'job-post-day')]").text
            except:

                posted_date = "NOT mentioned"

            try:
                job_summary = job.find_element("xpath", ".//span[contains(@class,'job-desc')]").text
            except:
                job_summary = "NOT mentioned"

            job_link = job.find_element("xpath", ".//a[contains(@class,'title')]").get_attribute("href")

            skills_list = job.find_elements("xpath", ".//ul[contains(@class,'tags-gt')]//li | .//ul[contains(@class,'tags-gt')]//a")
            skills = ', '.join([s.text for s in skills_list]) if skills_list else 'not found'

            writer.writerow(
                [job_title, company_name, location, experience, salary, posted_date, job_summary, job_link, skills])

        except Exception as E:
            print("ERROR EXTRACTING JOB", E)
    print("✅ Job data successfully saved to naukri_jobs.csv")

    driver.quit()
