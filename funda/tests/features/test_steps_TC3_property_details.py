from pytest_bdd import scenario, given, when, then, parsers


@scenario('smoke_tests.feature', 'Property details page loads')
def test_property_page_loads():
    pass



@given(parsers.parse('I am on the search results page for "{city}"'))
def on_property_listing_page(home_page, city): 
    home_page.navigate_to_property_listing_page(city)
    home_page.handle_cookie_popup()


@when('I click on the first property listing')
def open_property_details_page(property_listing_page):
    property_listing_page.open_property_details()



@then('verify the property details page loads successfully')
def verify_property_page(property_details_page):
    property_details_page.verify_property_details_page