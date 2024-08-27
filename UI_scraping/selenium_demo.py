from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configure WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode for no GUI

# Path to your ChromeDriver executable
service = Service('/home/brian/chromedriver-linux64')

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the web page
driver.get("http://localhost:3000/")

# Wait for the page to load completely
time.sleep(5)  # Adjust the sleep time if necessary

# Example: Extracting information from buttons
buttons = driver.find_elements(By.TAG_NAME, "button")
for button in buttons:
    print(f"Button text: {button.text}")

# Example: Extracting information from elements with specific classes or IDs
# This depends on the structure of your React app
# For example, if there's a section with class 'function-info':
try:
    function_info_elements = driver.find_elements(By.CLASS_NAME, "function-info")
    for element in function_info_elements:
        print(f"Function Info: {element.text}")
except Exception as e:
    print(f"Error extracting function info: {e}")

# Clean up and close the browser
driver.quit()