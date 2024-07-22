import time
# chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#unlock
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk

# Path to the ChromeDriver executable: USE YOURS
chrome_driver_path = 'C:/Users/pheda/Development/chromedriver.exe'

# Path to the MetaMask extension: USE YOURS
EXTENSION_PATH = 'C:/Users/pheda/automationtesting/nkbihfbeogaeaoehlefnkodbefgpgknn-11.16.14-Crx4Chrome.com.crx'
#YOUR METAMASK PASSWORD: USE YOURS
password = "Delight2012!"
#YOUR CHROME PROFILE: USE YOURS
CHROME_PATH = "C:/Users/pheda/AppData/Local/Google/Chrome/User Data"
# THE PROFILE THE EXTENSION WAS INSTALLED IN.:
EXACT_CHROME_PROFILE ="Profile 4"


# Initialize Chrome options
chrome_options = Options()
chrome_options.add_extension(EXTENSION_PATH)  # Load MetaMask extension
#Your chrome profile
chrome_options.add_argument(f"user-data-dir={CHROME_PATH}")
# The profile containing the extension
chrome_options.add_argument(f"profile-directory={EXACT_CHROME_PROFILE}")


network_name = "Arbitrum One"
RPC_URL= "https://arbitrum.llamarpc.com"
CHAIN_ID= "42161"
CURRENCY_SYMBOL="ETH"
BLOCK_EXPLORER_URL="https://arbiscan.io"


# Initialize WebDriver with Service
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the extension website : REPLACE THE ID "nkbihfbeogaeaoehlefnkodbefgpgknn" with your own extension id
EXTENSION_ID = "nkbihfbeogaeaoehlefnkodbefgpgknn"
driver.get(f"chrome-extension://{EXTENSION_ID}/home.html")



time.sleep(10)
password_field = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/form/div/div/input'))
)
password_field.send_keys(password)
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/button").click()
time.sleep(5)





# Perform actions in the third tab
WebDriverWait(driver, 30).until(
EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/button"))
).click()
WebDriverWait(driver, 30).until(
EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[3]/div[3]/div/section/div[3]/button"))
).click()

WebDriverWait(driver, 30).until(
EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[3]/div[3]/div/section/div[2]/div[2]/button"))
).click()


WebDriverWait(driver, 30).until(
EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[3]/div[3]/div/section/div[2]/div/div[1]/div/input"))
).click()

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section/div[2]/div/div[1]/div/input").send_keys("0x56ec2116b33eefed4e499d02f8f6f2bdb76b67d53406923e9aa9378dd1aa2fdc")
WebDriverWait(driver, 30).until(
EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[3]/div[3]/div/section/div[2]/div/div[2]/button[2]"))
).click()

WebDriverWait(driver, 30).until(
EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/button"))
).click()

WebDriverWait(driver, 30).until(
EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[3]/div[3]/div/section/div[5]/button"))
).click()

    # Scroll to bottom
time.sleep(5)
element_network = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/a/h6")
driver.execute_script("arguments[0].scrollIntoView(true);", element_network)
time.sleep(5)

WebDriverWait(driver, 30).until(
EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/a"))
).click()

time.sleep(3)
save_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]")

    # Scroll to bottom
driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input").send_keys(network_name)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input").send_keys(RPC_URL)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input").send_keys(CHAIN_ID)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/div/input").send_keys(CURRENCY_SYMBOL)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input").send_keys(BLOCK_EXPLORER_URL)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/section/div[2]/div/button[1]").click()
time.sleep(3)



time.sleep(8)

driver.get("https://console.brahma.fi/")
time.sleep(10)
# Click on collect wallet
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/button"))
).click()

# Click on Your recent wallet
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/button/div/div"))
).click()
time.sleep(7)
driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
time.sleep(8)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]"))
).click()

time.sleep(8)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]"))
).click()
time.sleep(8)
driver.get("https://console.brahma.fi/")



try:
    time.sleep(10)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div/button"))
    ).click()

    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[5]/footer/button[2]"))
    ).click()
    
    time.sleep(5)
    driver.get("https://console.brahma.fi/")
    time.sleep(10)

    ui_testing_console_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]")
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(ui_testing_console_button)
    ).click()




except Exception as e:
    print(f"Error navigating to UI-testing console: {e}")
    driver.quit()
    exit()

# Step 5: Take Screenshot
try:
    time.sleep(20)
    driver.save_screenshot("dashboard.png")
    time.sleep(5)
except Exception as e:
    print(f"Error taking screenshot: {e}")

# Step 6: Assert the $0.00 text
try:
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/p")
    assert element.text == "$0.00", "The text is not '$0.00'"
    print("Assertion passed: The text is '$0.00'")
except Exception as e:
    print(f"Assertion failed: {e}")


# Close WebDriver
driver.quit()








