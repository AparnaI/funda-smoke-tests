from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page import BasePage  # Adjust the import path as necessary


class ListingPage(BasePage):
    def __init__(self, driver, logger,timeout=10):
        super().__init__(driver, logger,timeout)
        self.driver = driver
        self.logger = logger


    PROPERTY = (By.XPATH, "//a[@data-testid = 'listingDetailsAddress']")

    def open_property_details(self):
        """Click on first property from listing"""
        self.wait_for_element_presence(*self.PROPERTY)
        property = self.driver.find_element(*self.PROPERTY)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(property).click().perform()
        self.logger.info("Navigated to property details page")