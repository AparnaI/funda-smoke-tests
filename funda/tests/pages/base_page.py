from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Base class for all pages to handle common functionalities."""
    
    def __init__(self, driver, logger,timeout=10):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, timeout)



    def wait_for_element(self, by, value):
        """Wait for an element to be visible within timeout."""
        try:
            return self.wait.until(EC.visibility_of_element_located((by, value)))
        except TimeoutException:
            raise Exception(f"Element {value} not found within timeout!")


    def wait_for_element_to_be_clickable(self, by, value):
        """Wait for an element to be clickable within timeout."""
        try:
            return self.wait.until(EC.element_to_be_clickable((by, value)))
        except TimeoutException:
            raise Exception(f"Element {value} not clickable within timeout!")
        
    
    def wait_for_element_presence(self, by, value):
        """Wait for the presence of an element in the DOM within timeout."""
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            raise Exception(f"Element {value} not present in the DOM within timeout!")