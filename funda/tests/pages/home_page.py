from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import time
from funda.tests.config import Config  

class HomePage(BasePage):

    def __init__(self, driver, logger, timeout=10):
        super().__init__(driver, logger, timeout)
        self.url = Config.BASE_URL
        self.logger = logger
        self.links = Config.LINKS


    # Locators on homepage
    SEARCH_BOX = (By.XPATH,"//*[@id = 'headlessui-combobox-input-v-0-0-0-0']")
    COOKIE_POPUP =  (By.ID,"didomi-notice-disagree-button")
    SEARCH_BOX_SUGGESTION = (By.XPATH, "//*[@data-testid = 'SearchBox-location-suggestion']")
    BODY = (By.TAG_NAME, 'body')


    def navigate_to_homepage(self):
        """Navigate to HomePage"""
        self.driver.get(self.url)
        self.logger.info("Navigated to funda.nl")

    
    def verify_page_title(self):
        """Verify the page title"""
        assert "funda" in self.driver.title, "Title is not as expected"
        self.logger.info("Homepage title verified")

    
    def handle_cookie_popup(self):
        """Handle cookie popup"""
        self.wait_for_element(*self.COOKIE_POPUP).click()


    def verify_search_box_is_visible(self):
        """Verify search box is displayed"""
        self.wait_for_element(*self.SEARCH_BOX)
        self.logger.info("Homepage loaded successfully")


    def search_for_city(self, city):
        """Search for city"""
        self.logger.info(f"Searching for {city}")
        search_box = self.wait_for_element(*self.SEARCH_BOX)
        search_box.send_keys(city)
        self.wait_for_element(*self.SEARCH_BOX_SUGGESTION)
        search_box.send_keys(Keys.ENTER)

        self.logger.info(f"Search results for {city} displayed")


    def navigate_to_property_listing_page(self,city):
        """Navigate to property listing page"""
        url = f'{self.url}zoeken/koop?selected_area=["{city}"]'
        self.driver.get(url)
        self.logger.info(f"Navigated to {city} property listing page")



    def verify_important_links_working(self):
         """To verify the important links are working"""
         for link in self.links:
   
            self.driver.execute_script("window.open(arguments[0]);", link)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.wait_for_element_presence(*self.BODY)

            self.logger.info(f"Link opened successfully: {link}")

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])