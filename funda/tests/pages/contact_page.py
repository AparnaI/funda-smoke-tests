from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):

    def __init__(self, driver,logger, timeout=10):
        super().__init__(driver, logger,timeout)
        self.driver = driver
        self.logger = logger


    def verify_contact_form(self):
        """Verify if contact form elements are displayed"""
        question_input = self.driver.find_element(By.CSS_SELECTOR, '#questionInput')
        checkbox = self.driver.find_element(By.ID, 'checkbox-viewingRequest')
        email = self.driver.find_element(By.ID, 'emailAddress')
        first_name = self.driver.find_element(By.ID, 'firstName')
        last_name = self.driver.find_element(By.ID, 'lastName')
        phone = self.driver.find_element(By.ID, 'phoneNumber')
        submit = self.driver.find_element(By.XPATH, "//button[@type = 'submit' and contains(@class,'inline-flex')]")

        elements = {
        "Question Input": question_input,
        "Checkbox": checkbox,
        "Email": email,
        "First Name": first_name,
        "Last Name": last_name,
        "Phone": phone,
        "Submit Button": submit,
         }

        for name, element in elements.items():
            assert element.is_displayed() and element.is_enabled(), f"{name} is not visible or not enabled"
            self.logger.info(f"{name} is visible and enabled")

        self.logger.info("Contact form verified successfully.")
