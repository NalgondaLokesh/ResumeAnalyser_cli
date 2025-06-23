from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Your dummy credentials
USERNAME = "doesnotmeantou"
PASSWORD = "Lokesh@0910"

# Set up Chrome WebDriver
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH

# Step 1: Open Instagram login
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Step 2: Login
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

# Step 3: Search for cbitosc
driver.get("https://www.instagram.com/cbitosc/")
time.sleep(5)

# Step 4: Follow if not already followed
try:
    follow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Follow']"))
    )
    follow_button.click()
    print("Followed cbitosc.")
    time.sleep(2)
except TimeoutException:
    print("Already following or button not found.")

# Step 5: Extract profile data
try:
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//header//h2 | //header//h1"))
    ).text
except TimeoutException:
    name = "Not found"

try:
    bio = driver.find_element(By.XPATH, "//header/section/div[contains(@class, 'x7a106z')]" ).text
except NoSuchElementException:
    try:
        bio = driver.find_element(By.XPATH, "//header/section/div[2]").text
    except NoSuchElementException:
        bio = "Not found"

try:
    stats = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//header/section/ul/li"))
    )
    posts = stats[0].text.split(" ")[0]
    followers = stats[1].text.split(" ")[0]
    following = stats[2].text.split(" ")[0]
except Exception:
    posts = followers = following = "Not found"

# Step 6: Save data to file
with open("cbitosc_profile.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Bio: {bio}\n")
    file.write(f"Posts: {posts}\n")
    file.write(f"Followers: {followers}\n")
    file.write(f"Following: {following}\n")

print("Profile data saved to cbitosc_profile.txt")

# Cleanup
driver.quit()
