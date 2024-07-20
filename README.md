# Junior QA Automation Script

## Overview

This repository contains an automation script designed for testing the Brahma Console application using Selenium WebDriver with Python. The script performs the following actions:

1. Loads the Brahma Console URL.
2. Interacts with MetaMask for wallet connection and network setup.
3. Signs a message.
4. Navigates to the UI-testing console.
5. Takes a screenshot of the dashboard.
6. Asserts that the displayed text is "$0.00".

## Prerequisites

- Python (version 3.6 or higher)
- Selenium library
- Tkinter library
- ChromeDriver executable


### Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name


## Install Dependencies
Ensure you have Python installed. Then install the required Python packages using pip:
pip install selenium
pip install tk

Script imports:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    import tkinter as tk
    ....


Download and place the chromedriver.exe file in the same directory as this script or specify its path in the chrome_driver_path variable.

Update Script Variables
Open automation_script.py and ensure the chrome_driver_path variable points to your chromedriver.exe file:
chrome_driver_path = 'path/to/chromedriver.exe'

Also, ensure that the MetaMask wallet details and the Arbitrum RPC URL are correct and up-to-date.

Running the Script
Open Terminal/Command Prompt

Navigate to the directory containing automation_script.py.

Run the Script

Execute the script with Python:

python automation_script.py
The script will open a Chrome browser and perform the automation steps. Follow the instructions in the Tkinter pop-up windows to complete the MetaMask configuration.

Manual Steps
During execution, you will need to manually perform the following actions:

1. MetaMask Configuration:

    Configure MetaMask with the provided details.
    Add the Arbitrum network and import the provided account.
    Switch to the Arbitrum network.
    Verify and Select Account:

2. Verify and select the correct account in MetaMask.
    Click "Next" and confirm the transaction on the new window or popup.
    Confirm Signature:

3. Confirm the signature in MetaMask when prompted.


### Key Points to Ensure Proper Execution:
1. **Dependencies and Path Setup:**
   - Make sure all dependencies are installed.
   - Verify that the path to `chromedriver.exe` is correctly specified in the script.

2. **MetaMask Configuration:**
   - Users must manually configure MetaMask and follow the prompts as described.

3. **Running the Script:**
   - Run the script from the command line in the directory where the script is located.

4. **Troubleshooting:**
   - Ensure compatibility between ChromeDriver and the Chrome browser.
   - Adjust paths and settings as needed based on individual system configurations.

By following these instructions, users should be able to set up and run the automation script successfully.


Contact
For questions or issues, please contact phedave05@gmail.com







