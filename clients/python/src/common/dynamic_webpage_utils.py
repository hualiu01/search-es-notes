"""
For JS rendered webpages, we need to use Google Chrome driver to download the webpage.

"""
from common.os_utils import get_required_env_var
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger(__name__)

PATH_TO_CHROME_DRIVER = get_required_env_var("PATH_TO_CHROME_DRIVER")
LOCAL_CHROME_DRIVER_VERSION = get_required_env_var("LOCAL_CHROME_DRIVER_VERSION")
logger.info(f"loaded chrome driver version {LOCAL_CHROME_DRIVER_VERSION} from {PATH_TO_CHROME_DRIVER}")

def dynamic_query_url_with_chrome_driver_and_save(url, save_to):

    # Specify custom Chrome location
    chrome_options = Options()
    chrome_options.binary_location = "/Applications/Google Chrome.app"  # Update path if needed


    # Specify the path to ChromeDriver
    service = Service(PATH_TO_CHROME_DRIVER)  # Update this path as needed
    driver = webdriver.Chrome(service=service)

    # Open the desired webpage
    driver.get(url)

    # Get the page source (HTML content)
    page_source = driver.page_source

    # Save the HTML content to a local file
    with open(save_to, "w", encoding="utf-8") as file:
        file.write(page_source)

    print(f"Webpage saved as '{save_to}'")

    # Close the browser
    driver.quit()
    