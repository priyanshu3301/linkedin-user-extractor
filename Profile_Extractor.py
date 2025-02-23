import re
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

# Function to extract LinkedIn domain from a URL
def extract_linkedin_domain(url):
    pattern = r'([a-zA-Z0-9-]+\.linkedin\.com)'
    match = re.search(pattern, url)
    return match.group(0) if match else None

# Function to extract links from a webpage and save them to a CSV file without duplicates
def extract_links_and_save_to_csv(driver, filename, domain):
    # Find all anchor tags with the 'href' attribute
    links = driver.find_elements(By.TAG_NAME, "a")
    hrefs = set()  # Use a set to avoid duplicates

    # Extract each link's 'href' attribute
    for link in links:
        href = link.get_attribute("href")
        if href and href.startswith(f'https://{domain}'):
            hrefs.add(href)

    # Write unique links to a new CSV file
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for href in hrefs:
            csv_writer.writerow([href])
    print("Links extracted and saved to CSV successfully.")

# Function to automatically click "More results" until no more results are available
def auto_more(driver, filename, domain):
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    
    while True:
        try:
            # Locate the "More results" link
            more_results_link = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.T7sFge.sW9g3e.VknLRd[jsname='oHxHid'][aria-label='More results']")
            ))
            # Perform double-click action
            actions.double_click(more_results_link).perform()
            # Wait for a short duration to allow the style change to occur
            time.sleep(1)
            # Check if the style attribute indicates that more results are no longer available
            style = more_results_link.get_attribute("style")
            if "transform: scale(0);" in style:
                break
        except TimeoutException:
            print("No more results link found or operation timed out.")
            break
    extract_links_and_save_to_csv(driver, filename, domain)

# Function to check if CAPTCHA is present
def is_captcha_present(driver):
    try:
        driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
        return True
    except NoSuchElementException:
        return False
    
 #Login Activity   
def login_linkedin(username, password, driver):

    try:
        # Open LinkedIn login page
        driver.get("https://www.linkedin.com/login")

        # Find and fill the username field
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)

        # Find and fill the password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the page to load and check for the title "Security Verification | LinkedIn"
        WebDriverWait(driver, 10).until(EC.title_contains("LinkedIn"))

        # Check if the security verification page is displayed
        if "Security Verification | LinkedIn" in driver.title:
            print("CAPTCHA detected. Please solve it in the browser.")
            # Wait until the title changes indicating that the user has solved the CAPTCHA
            while "Security Verification | LinkedIn" in driver.title:
                time.sleep(5)  # Wait and check again every 5 seconds
            print("CAPTCHA solved. Resuming operation.")
            if "Restriction | LinkedIn" in driver.title:
                print("Linkedin Ban your Account\nMake a new One then try agin")
                exit(0)
                

        # Continue with any other operations on LinkedIn after logging in
        print("Logged in successfully.")
    except:
        print("Something Wrong\nRerun the code")
        exit(0)

def extract(link, t):
    try:
        driver.get(link)  # Navigate to the profile link
        time.sleep(5)
        
        # Define XPaths for name, company, location, and premium indicator (adjust if needed)
        name_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span/a/h1'
        company_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]'
        loc_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/ul/li/button/span/div'
        premium_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[1]/div[2]/div/span/span'

        # Wait for elements to be visible
        wait = WebDriverWait(driver, 10)
        name_element = wait.until(EC.visibility_of_element_located((By.XPATH, name_xpath)))
        company_element = wait.until(EC.visibility_of_element_located((By.XPATH, company_xpath)))
        loc_element = wait.until(EC.visibility_of_element_located((By.XPATH, loc_xpath)))

        # Try to find the premium element, set default to 'NO' if not found
        try:
            premium_element = wait.until(EC.visibility_of_element_located((By.XPATH, premium_xpath)))
            premium = 'YES'
        except:
            premium = 'NO'
            print(f'{link} not a premium user')

        # Extract text from elements (if found)
        name = name_element.text if name_element else 'N/A'
        company = company_element.text if company_element else 'N/A'
        loc = loc_element.text if loc_element else 'N/A'

        # Save data to CSV
        with open('linkedin_final.csv', "a", newline="", encoding="utf-8") as csvfile:
            t = t + 1
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([t, name, company, loc, premium, link])
            print('user no ', t)
            print(f"Successfully extracted data for: {link}")

    except Exception as e:
        print(f"Error extracting data for link: {link}. Skipping to next link. Error: {e}")

    finally:
        return t


# Main script
if __name__ == "__main__":
    url = input("Enter URL: ")
    # For potential delays between profile visits
    email = input("Enter Linkedin Email = ")
    pw = input("Enter Linkedin Password = ")
    driver = webdriver.Chrome()
    driver.get(url)
    filename = "extracted_links.csv"

    # Extract LinkedIn domain from the URL
    domain = extract_linkedin_domain(url)
    if not domain:
        print("Invalid LinkedIn URL")
        driver.quit()
        exit()

    # Check for CAPTCHA
    if is_captcha_present(driver):
        print("CAPTCHA detected. Please solve it in the browser.")
        while is_captcha_present(driver):
            time.sleep(5)  # Wait and check again every 5 seconds
        print("CAPTCHA solved. Resuming operation.")

    # Start the automatic "More results" process
    auto_more(driver, filename, domain)
    #login 
    login_linkedin(email, pw, driver)

    #counter
    t=0
    # Open the CSV file containing links
    with open(filename, "r", newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:  # Iterate over each row
            link = row[0]  # Extract the link from the row
            t = extract(link, t)
            if t == 100:
                break

    # Close the driver
    driver.quit()
