import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.edge.service import Service
import logging
from funda.tests.pages.home_page import HomePage
from funda.tests.pages.search_result_page import SearchPage
from funda.tests.pages.listing_page import ListingPage
from funda.tests.pages.property_deatils_page import PropertyPage
from funda.tests.pages.contact_page import ContactPage


@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger("funda_qa_automation")
    logger.setLevel(logging.INFO)  # Log at INFO level
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logger


@pytest.fixture(scope='function')
def driver(logger):
    options = Options()
    options.add_argument("--start-maximized")
    #add user-agent option to bypass robot detection
    #options.add_argument("user-agent = {replace with secret}")
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
    logger.info("Setting up Edge browser...")
    yield driver
    logger.info("Quitting Edge browser...")
    driver.quit()

@pytest.fixture(scope='function')
def home_page(driver,logger):
    return HomePage(driver,logger)

@pytest.fixture(scope='function')
def search_result_page(driver,logger):
    return SearchPage(driver,logger)

@pytest.fixture(scope='function')
def property_listing_page(driver,logger):
    return ListingPage(driver,logger)


@pytest.fixture(scope='function')
def property_details_page(driver,logger):
    return PropertyPage(driver,logger)

@pytest.fixture(scope='function')
def contact_page(driver,logger):
    return ContactPage(driver,logger)