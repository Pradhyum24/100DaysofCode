from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ACCOUNT_EMAIL = "@gmail.com"
ACCOUNT_PASSWORD = "@"

# Optional: Keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# Open LinkedIn job search page
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4225870684&distance=25&f_AL=true&f_E=2&geoId=105556991&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY")
# Wait for the "Sign in" button and click it
wait = WebDriverWait(driver, 3)

# Wait until overlay is invisible, if present
try:
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal__overlay--visible")))
except:
    pass  # If it doesn't exist, continue anyway

sign_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
driver.execute_script("arguments[0].click();", sign_in_button)

email_address = driver.find_element(By.ID,value="username")
email_address.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.ID,value="password")
password.send_keys(ACCOUNT_PASSWORD)

sign_in_button = driver.find_element(By.CLASS_NAME,value="btn__primary--large")
sign_in_button.click()

time.sleep(4)
easy_apply = driver.find_element(By.ID,value="jobs-apply-button-id")
easy_apply.click()
wait = WebDriverWait(driver, 5)


try:
    next_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button//span[text()="Next"]/..')))
    time.sleep(1)  # give UI time to settle
    driver.execute_script("arguments[0].click();", next_button)
except Exception as e:
    print("Retry failed to click Next button:", e)

try:
    next_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button//span[text()="Next"]/..')))
    time.sleep(1)  # give UI time to settle
    driver.execute_script("arguments[0].click();", next_button)
except Exception as e:
    print("Retry failed to click Next button:", e)

dropdown = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID,
        "text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4228489732-18377485722-multipleChoice"
    ))
)

# Select "Yes" from the dropdown
select = Select(dropdown)
select.select_by_visible_text("Yes")
print("✅ Selected 'Yes' in the dropdown.")

# Wait for and click the "Review" button
review_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Review"]]'))
)
driver.execute_script("arguments[0].click();", review_button)
print("✅ Clicked 'Review' button.")

submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Submit application')]"))
)
submit_button.click()
