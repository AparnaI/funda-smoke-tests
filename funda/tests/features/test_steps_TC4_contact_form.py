from pytest_bdd import scenario, given, when, then, parsers
import pytest


@pytest.mark.smoke
@scenario('smoke_tests.feature', 'Contact form is displayed')
def test_contact_form():
    pass


@given(parsers.parse('I am on a property details page of "{city}"'))
def on_property_details_page(city,home_page,property_listing_page,property_details_page):
    home_page.navigate_to_property_listing_page(city)
    home_page.handle_cookie_popup()
    property_listing_page.open_property_details()
    property_details_page.verify_property_details_page()


@when('I click on the contact button')
def open_contact_page(property_details_page):
    property_details_page.open_contact_form()

    

@then('the contact form should be displayed and verfied')
def verify_contact_form(contact_page):
    contact_page.verify_contact_form()