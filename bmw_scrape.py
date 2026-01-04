import csv
import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import random

import re

# ------ Prepare the csv file ------

file_name = 'bmw_540i.csv'

# Create the header row
header = ['Year', 'Price', 'Mileage', 'Trim']

with open(file_name, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

# ------ Driver setup ------

options = Options()
options.add_argument("--start-maximized")
service = Service(r"C:\Windows\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=options)

url = "https://www.bmwusa.com/certified-preowned-search/zip"
driver.get(url)

input("Once you see the list of cars, press Enter here in the terminal to start...")

# ------ Data Scraping ------

i = 0
wait = WebDriverWait(driver, 10)
listing_selector = "div[class^='_vehicletile']"

while True:
    # find all listings of the current page
    listings = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, listing_selector))
    )
    print(f"Processing {len(listings)} cars on this page...")

    for car in listings:
        i += 1
        print(f"Scraping car #{i}")

        # ------ scrape data: price, mileage ------
        details = car.find_elements(By.CLASS_NAME, "content-2")

        price = details[0].text
        mileage = details[1].text

        print(f"Scraped: {price} | {mileage}")

        # ------ open the detail page in a new tab ------
        # find the button
        detail_button = car.find_element(By.CSS_SELECTOR, "a[class^='_detailbutton']")

        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).click(detail_button).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[-1])

        # ------ scrape the year and trim ------
        title_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "headline-5--bold"))
        )
        year = title_element.text[:4]  # Grabs "20xx"

        # Get the Drivetrain (Trim)
        trim_element = driver.find_element(By.XPATH, "//div[text()='Drivetrain']/following-sibling::div")
        trim = trim_element.text

        print(f"Year: {year} | Trim: {trim}")

        # ------ Close the tab ------
        time.sleep(random.uniform(10.0, 30.0))      # stay for a random moment to agianst Anti-bot
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        # ------ Save data into csv file ------
        row_to_save = [year, price, mileage, trim]

        with open(file_name, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(row_to_save)

        print(f"Successfully saved {year} BMW to CSV.")

        # wait a moment before next car scraping
        time.sleep(random.uniform(2.5, 5.0))

    # After the inner loop finishes all 20 cars, find the Next button
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next Results Page']")
        # driver.execute_script("arguments[0].scrollIntoView();", next_btn)
        next_btn.click()
        time.sleep(random.uniform(5.0, 13.0)) # Wait for Page 2, 3, etc. to load
    except:
        # This runs if 'next_btn' isn't found or isn't clickable
        print("Reached the final page. Script complete!")
        break

driver.quit()
print("Done Scraping")