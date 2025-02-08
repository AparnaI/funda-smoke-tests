from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class PropertyPage(BasePage):
    
    def __init__(self, driver,logger, timeout=10):
        super().__init__(driver, logger,timeout)
        self.driver = driver
        self.logger = logger

    PHOTOS = (By.XPATH,"//*[@data-testid='photos']")
    CONTACT = (By.XPATH,"//*[contains(@href,'makelaar-contact')]")

   
    def verify_property_details_page(self):  
        """Validate Photos and Contact on Property page"""     
        photos = self.wait_for_element(*self.PHOTOS)
        assert photos.is_displayed(), "Photos are not displayed"
        contact = self.wait_for_element(*self.CONTACT)
        assert contact.is_displayed(), "Contact button is not displayed"
        self.logger.info('Details page is verified')


    def open_contact_form(self):
        """Open Contact form on property details page"""
        contact = self.driver.find_element(*self.CONTACT)
        action = ActionChains(self.driver)
        action.move_to_element(contact).click().perform()
        self.logger.info("Navigated to contact page")
