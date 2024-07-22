# Junior QA Automation Script

## Overview

This repository contains an automation script designed for testing the Brahma Console application using Selenium WebDriver with Python. The script performs the following actions:

- Loads the Brahma Console URL.
- Interacts with MetaMask for wallet connection and network setup.
- Navigates to the UI-testing console.
- Takes a screenshot of the dashboard.
- Asserts that the displayed text is "$0.00".

## Prerequisites

Before running the script, ensure you have the following:

- Python (version 3.6 or higher)
- Selenium library
- ChromeDriver executable
- MetaMask extension (CRX file)

## MetaMask Extension Setup

1. **Download MetaMask Extension:**
   - Go to the [MetaMask website](https://metamask.io/) or the [Chrome Web Store](https://chrome.google.com/webstore/category/extensions) to download the MetaMask extension.

2. **Install MetaMask:**
   - Install MetaMask in your Chrome browser by dragging the `.crx` file into the Chrome extensions page (`chrome://extensions/` with Developer mode enabled).
   - Create a new MetaMask account or import an existing one. 

3. **Obtain MetaMask Extension ID:**
   - Navigate to `chrome://extensions/` in your Chrome browser.
   - Enable "Developer mode" at the top-right corner.
   - Find the MetaMask extension and note its ID (a string of letters and numbers). 

4. **Store the CRX File:**
   - Save the downloaded MetaMask CRX file in a directory on your system. Note the path to this file for use in the script.
5. Update the Script URL:
    Replace the placeholder extension ID in the script with your MetaMask extension ID. The URL format will be:
        driver.get(f"chrome-extension://{YOUR_EXTENSION_ID}/home.html")
        Ensure to replace YOUR_EXTENSION_ID with the actual ID you copied.

## ChromeDriver Setup

1. **Download ChromeDriver:**
   - Download the appropriate version of ChromeDriver that matches your Chrome browser version from the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).

2. **Store ChromeDriver:**
   - Save `chromedriver.exe` in a directory on your system. Note the path to this file for use in the script.

## Script Configuration

1. **Update Script Variables:**
   - Open `main.py` and update the following variables with the paths and MetaMask account details:

     ```python
     chrome_driver_path = 'path/to/chromedriver.exe'
     EXTENSION_PATH = 'path/to/metamask-extension.crx'
     ```

   - **Ensure to replace `EXTENSION_PATH` with the path to your MetaMask CRX file.**

   - **MetaMask Account Details:**
     - **Do not use the MetaMask password provided in any example or public documentation. Ensure you use your own MetaMask account credentials and password.

2. **Update MetaMask Extension ID:**
   - Replace the variable extension ID in the script with the actual MetaMask extension ID retrieved from `chrome://extensions/`.

## Steps to Run the Script

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2.Install Dependencies:
    Ensure you have Python installed. Then install the required Python packages using pip:
    pip install selenium
3. Execute the script with Python:
    python main.py
    
The script will open a Chrome browser and perform the automation steps. Ensure MetaMask is properly configured and the extension is loaded as specified in the script.
**Key Points to Ensure Proper Execution:**
Dependencies and Path Setup:

Ensure all dependencies are installed.
Verify that the paths to chromedriver.exe and the MetaMask CRX file are correctly specified in the script.
MetaMask Configuration:

MetaMask must be installed and configured as described. The script will handle the rest automatically.
Running the Script:

Execute the script from the command line in the directory where main.py is located.
Troubleshooting:
Ensure compatibility between ChromeDriver and the Chrome browser.
Adjust paths and settings as needed based on your system configuration.
By following these instructions, users should be able to set up and run the automation script successfully.

Contact
For questions or issues, please contact: phedave05@gmail.com
