from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page import BasePage
import time

class SearchPage(BasePage):

    #locators on search results page
    FILTER_PANEL = (By.XPATH,"//div[@id = 'FilterPanel']")
    PROPERTY_LISTING = (By.XPATH,"//a[@data-testid = 'listingDetailsAddress']")
    PAGINATION = (By.XPATH, "//*[@data-testid = 'pagination']")
                    
       
    def __init__(self, driver,logger, timeout=10):
        super().__init__(driver, logger,timeout)
        self.driver = driver
        self.logger = logger

    

    def verify_search_results_page(self, city):
        self.wait_for_element(*self.FILTER_PANEL)
        self.wait_for_element_presence(*self.PAGINATION)
        print(f"Search result page title is {self.driver.title}")
        assert city in self.driver.title, "Search result page title is not as expected"
        self.logger.info('Search result page is verified')


        
    
    def verify_properties_are_listed(self):
        self.logger.info(f"Checking if properties are listed")
        property_listing = self.driver.find_elements(*self.PROPERTY_LISTING)
        assert len(property_listing) > 0, "No property listings found"
        self.logger.info(f"Properties are listed")



    def verify_pagination_is_enabled(self):
        self.wait_for_element(*self.PAGINATION)
        pagination = self.driver.find_element(*self.PAGINATION)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(pagination).perform()
        assert pagination.is_enabled(), "Pagination is not interactable"           
        self.logger.info("Pagination is enabled")