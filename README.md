Here’s a well-structured `README.md` format you can follow for your LinkedIn User Info Extractor project:

---

# **LinkedIn User Info Extractor**  

## **Table of Contents**  
- [Introduction](#introduction)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [How It Works](#how-it-works)  
- [File Structure](#file-structure)  
- [Error Handling](#error-handling)  
- [Limitations](#limitations)  
- [Disclaimer](#disclaimer)  
- [License](#license)  

---

## **Introduction**  
This Python script automates LinkedIn profile data extraction using **Selenium WebDriver**. It logs into LinkedIn, scrapes public profile information, and saves extracted data into a **CSV file**.  

---

## **Features**  
✔ **Automated Login:** Logs into LinkedIn with user credentials.  
✔ **Profile Link Extraction:** Extracts unique LinkedIn profile links from a search page.  
✔ **CAPTCHA Detection:** Detects CAPTCHA and prompts manual resolution.  
✔ **Automated "More Results" Clicking:** Loads more profiles automatically.  
✔ **User Data Extraction:** Extracts Name, Company, Location, and Premium Status.  
✔ **CSV Output:** Saves extracted data into `linkedin_final.csv`.  

---

## **Prerequisites**  
Ensure you have the following installed:  

- **Python 3.x**  
- **Google Chrome** (latest version)  
- **ChromeDriver** (matching your Chrome version)  
- **Python Libraries:**  
  Install required dependencies using:  
  ```bash
  pip install selenium
  ```

---

## **Installation**  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/linkedin-user-extractor.git
   cd linkedin-user-extractor
   ```
2. **Install Dependencies:**  
   ```bash
   pip install selenium
   ```
3. **Set Up ChromeDriver:**  
   - Download **ChromeDriver** from [here](https://sites.google.com/chromium.org/driver/).  
   - Add it to your **system PATH** or update the script with its location.  

---

## **Usage**  

1. **Run the Script:**  
   ```bash
   python your_script.py
   ```
2. **Provide Required Inputs:**  
   - **LinkedIn URL** (e.g., search result page)  
   - **Email & Password** (for LinkedIn login)  
3. **Automated Process:**  
   - Extracts profile links from the search results.  
   - Logs into LinkedIn.  
   - Visits each profile and extracts data.  
   - Saves results in **`linkedin_final.csv`**.  

---

## **How It Works**  

| Function | Description |
|----------|------------|
| `extract_linkedin_domain(url)` | Extracts the LinkedIn domain from a given URL. |
| `extract_links_and_save_to_csv(driver, filename, domain)` | Scrapes LinkedIn profile links and saves them in a CSV file. |
| `auto_more(driver, filename, domain)` | Clicks the "More results" button until no more profiles load. |
| `is_captcha_present(driver)` | Checks if a CAPTCHA is present on LinkedIn. |
| `login_linkedin(username, password, driver)` | Logs into LinkedIn and handles CAPTCHA manually if required. |
| `extract(link, t)` | Extracts Name, Company, Location, and Premium Status from a profile page. |
| **Main Script** | Orchestrates the full process, stops after extracting 100 profiles or when no links remain. |

---

## **File Structure**  
```
linkedin-user-extractor/
│── extracted_links.csv  # Stores extracted profile links
│── linkedin_final.csv   # Stores extracted user data
│── your_script.py       # Main Python script
│── README.md            # Project documentation
```

---

## **Error Handling**  
- If CAPTCHA is detected, the script prompts manual resolution.  
- If **LinkedIn blocks access**, you may need to use a new account.  
- If extraction fails for a profile, the script skips it and continues.  

---

## **Limitations**  
⚠ **LinkedIn Terms of Service:** This script may violate LinkedIn policies. Use it responsibly.  
⚠ **CAPTCHA Restrictions:** LinkedIn may detect automation and prompt CAPTCHA verification.  
⚠ **Account Restrictions:** Frequent use may result in **temporary bans**.  

---

## **Disclaimer**  
This tool is for **educational and research purposes only**. The author is **not responsible** for misuse. Ensure compliance with **LinkedIn’s policies and applicable laws** before using this script.  


### 🚀 Happy Scraping! 🚀