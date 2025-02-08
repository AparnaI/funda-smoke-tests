from pytest_bdd import scenario, given, when, then, parsers
import pytest


@pytest.mark.smoke
@scenario('smoke_tests.feature', 'Important links are working on homepage')
def test_important_links():
    pass



@given('I am on the Funda homepage')
def on_homepage(home_page):
    home_page.navigate_to_homepage()
    home_page.verify_page_title()
    home_page.handle_cookie_popup()


@then('Verify all important links are working')
def verify_links(home_page):
    home_page.verify_important_links_working()