from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Set up your LinkedIn credentials
linkedin_username = 'chetanchoudharie@gmail.com'
linkedin_password = 'cc29121995'

# Set up the WebDriver (make sure the path to your chromedriver is correct)
service = Service('/random/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# LinkedIn login function
def linkedin_login():
    driver.get('https://www.linkedin.com/login')
    time.sleep(5)

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(linkedin_username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(linkedin_password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

# Function to add connections from My Network page
def add_connections():
    while True:  # Infinite loop
        driver.get('https://www.linkedin.com/mynetwork/')
        time.sleep(7)

        # Scroll down to load more profiles
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        # Find and click 'Connect' buttons
        connect_buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Invite')]")
        for button in connect_buttons:
            try:
                button.click()
                time.sleep(4)
            except Exception as e:
                print(f"Error: {e}")

        # Optional: Wait before the next iteration
        time.sleep(60)  # Wait 60 seconds before running the loop again

# Main execution
try:
    linkedin_login()
    add_connections()  # This will run indefinitely
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
