from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Setup ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode (no GUI)
service = Service('path/to/chromedriver')  # Replace with the path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define test variables
url = "https://practicetestautomation.com/practice-test-login"  # URL
username = "student"            # test data for username
password = "Password123"        # test data for password

try:
    # Open the web page
    driver.get(url)

    # Find username and password fields and the login button
    username_field = driver.find_element(By.ID, "username")  # Enter username
    password_field = driver.find_element(By.ID, "password")  # Enter password
    login_button = driver.find_element(By.ID, "submit")      # Click submit button

    # Input credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Wait for the login process to complete (simplistic approach)
    driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to be available

    # Check for successful login
    try:
        # Validate that 'Logged In Successfully' text message is displayed on screen
        welcome_message = driver.find_element(By.XPATH, "//h1[text()='Logged In Successfully']")
        print("Login successful!")
    except NoSuchElementException:
        print("Login failed or welcome message not found.")

finally:
    # Close the browser
    driver.quit()