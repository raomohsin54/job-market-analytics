from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Step 1: Cities to scrape
cities = {
    "Perth": "6010",
    "Sydney": "2000",
    "Melbourne": "3000"
}

# Step 2: Setup Chrome driver options
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # enable if needed

driver_path = r"C:\Users\mmukhtiar\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Step 3: Scraping logic
job_data = []

for city in cities.keys():
    url = f"https://www.seek.com.au/data-jobs/in-{city.lower()}"
    print(f"\n🔍 Scraping jobs for {city}...\n")

    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'article[data-automation="normalJob"]'))
        )

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        jobs = driver.find_elements(By.CSS_SELECTOR, 'article[data-automation="normalJob"]')
        print(f"✅ Found {len(jobs)} jobs in {city}.")

        for job in jobs:
            try:
                title = job.find_element(By.CSS_SELECTOR, 'a[data-automation="jobTitle"]').text
            except NoSuchElementException:
                title = "N/A"

            try:
                company = job.find_element(By.CSS_SELECTOR, 'a[data-automation="jobCompany"]').text
            except NoSuchElementException:
                company = "N/A"

            try:
                location = job.find_element(By.CSS_SELECTOR, '[data-automation="jobLocation"]').text
            except NoSuchElementException:
                location = "N/A"

            try:
                summary = job.find_element(By.CSS_SELECTOR, 'div[data-automation="jobShortDescription"]').text
            except NoSuchElementException:
                summary = "N/A"

            try:
                salary = job.find_element(By.CSS_SELECTOR, 'span[data-automation="jobSalary"]').text
            except NoSuchElementException:
                salary = "N/A"

            try:
                date_posted = job.find_element(By.CSS_SELECTOR, 'span[data-automation="jobListingDate"]').text
            except NoSuchElementException:
                date_posted = "N/A"

            try:
                link = job.find_element(By.CSS_SELECTOR, 'a[data-automation="jobTitle"]').get_attribute('href')
            except NoSuchElementException:
                link = "N/A"

            job_data.append({
                'City': city,
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Summary': summary,
                'Salary': salary,
                'Date Posted': date_posted,
                'Link': link
            })

            print(f"📄 {title} | {company} | {location}")

    except TimeoutException:
        print(f"❌ No jobs found or page load timed out for {city}.")

    time.sleep(2)

driver.quit()

# Step 4: Save results
df = pd.DataFrame(job_data)
output_file = r"C:\Users\mmukhtiar\Downloads\Projects\job-market-analytics\WebScraper\seek_jobs.csv"
df.to_csv(output_file, index=False)

print(f"\n💾 Saved {len(df)} jobs to {output_file}")
