from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk


# Correct path to the ChromeDriver executable
chrome_driver_path = 'C:/Users/pheda/Development/chromedriver.exe'

# Initialize WebDriver with Service
service = Service(executable_path=chrome_driver_path)
# chrome_options.add_argument("--load-extension=" + metamask_extension_path)


driver = webdriver.Chrome(service=service)


# Load Brahma Console
driver.get("https://console.brahma.fi")

# Click on collect wallet
WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/button"))
).click()

# Click on the Metamask wallet
WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/button/div/div"))
).click()

#Click on get
WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[2]/button/div"))
).click()

# Click on Add to chrome
WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div/div[1]/div[3]/div[2]/div[3]/a/div"))
).click()


# Click on Add to chrome in the Chrome extention shop website
handles = driver.window_handles
driver.switch_to.window(handles[1])
WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/main/div/section[1]/section/div[2]/div/button'))
).click()
# Step 2: Pause for manual MetaMask configuration using Tkinter
def show_message():
    def on_ok():
        root.destroy()

    def on_cancel():
        root.destroy()
        driver.quit()
        exit()

    root = tk.Tk()
    root.title("MetaMask Configuration")

    instructions = (
        "Please configure MetaMask manually:\n\n"
        "1. Once installed, click on the MetaMask extension and sign in or set up a new account.\n\n"
        "2. Once you are on your MetaMask dashboard and have completed the setup, click OK to continue.\n\n"
        "3. In the MetaMask extension, go to 'Settings' > 'Networks' > 'Add Network'.\n\n"
        "4. Enter the following details:\n"
        "   - Network Name: Arbitrum One\n"
        "   - New RPC URL: https://arbitrum.llamarpc.com\n"
        "   - Chain ID: 42161\n"
        "   - Currency Symbol: ETH\n"
        "   - Block Explorer URL: https://arbiscan.io\n\n"
        "5. After configuring the network, import the provided account using the private key: 0x56ec2116b33eefed4e499d02f8f6f2bdb76b67d53406923e9aa9378dd1aa2fdc.\n\n"
        "6. Finally, switch to the Arbitrum network and click OK to continue."
    )

    text_widget = tk.Text(root, wrap=tk.WORD)
    text_widget.insert(tk.END, instructions)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(padx=20, pady=20)
    
    ok_button = tk.Button(root, text="OK", command=on_ok)
    ok_button.pack(side=tk.LEFT, padx=20, pady=20)

    cancel_button = tk.Button(root, text="Cancel", command=on_cancel)
    cancel_button.pack(side=tk.RIGHT, padx=20, pady=20)

    root.mainloop()


#Triggers the show_message function
show_message()

# Delay for 3 seconds
time.sleep(5)


# Return to the main/first window
driver.switch_to.window(handles[0])

# Refresh the site
WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[2]/button"))
).click()

#Click on collect wallet
WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/button"))
).click()

# Click on Your recent wallet
WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/button/div/div"))
).click()

WebDriverWait(driver, 90).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/button/div/div"))
).click()


# Pause for manual configuration: Click the confirm button on the new window or popup
def confirm_action():
    def on_ok():
        root.destroy()

    def on_cancel():
        root.destroy()
        driver.quit()
        exit()

    root = tk.Tk()
    root.title("MetaMask Configuration")

    instructions = (
        "Please configure MetaMask manually:\n\n"
        "1. Please select account 2 and click on Next \n\n"
        "2. Please click on Confirm.\n\n"
        "3. You will be redirected to a different page, once you are there, and you can see the title "Secured with signature", please click on 'Ok' to continue \n\n"

    )

    label = tk.Label(root, text=instructions, justify=tk.LEFT)
    label.pack(padx=20, pady=20)

    ok_button = tk.Button(root, text="OK", command=on_ok)
    ok_button.pack(side=tk.LEFT, padx=20, pady=20)

    cancel_button = tk.Button(root, text="Cancel", command=on_cancel)
    cancel_button.pack(side=tk.RIGHT, padx=20, pady=20)

    root.mainloop()


#Triggers the confirm_action function
confirm_action()





# Step 3: Sign Message
try:
    time.sleep(10)
    sign_message_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/button")
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(sign_message_button)
    ).click()

    time.sleep(10)

# Pause for manual configuration: Confirm Signature
    def confirm_sign():
        def on_ok():
            root.destroy()

        def on_cancel():
            root.destroy()
            driver.quit()
            exit()

        root = tk.Tk()
        root.title("MetaMask Configuration")

        instructions = (
            "Please configure Your Signature manually:\n\n"
            "1. Confirm Your signature \n\n"
            "2. You will be redirected to page, once you are there, and you can seee two consoles "Manual and UI testing", please click on ok to continue. \n\n"

        )

        label = tk.Label(root, text=instructions, justify=tk.LEFT)
        label.pack(padx=20, pady=20)

        ok_button = tk.Button(root, text="OK", command=on_ok)
        ok_button.pack(side=tk.LEFT, padx=20, pady=20)

        cancel_button = tk.Button(root, text="Cancel", command=on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=20, pady=20)

        root.mainloop()


    # Triggers the confirm_sign function
    confirm_sign()


except Exception as e:
    print(f"Error during sign message step: {e}")
    driver.quit()
    exit()

# Step 4: Select UI-testing console
try:
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
