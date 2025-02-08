from pytest_bdd import scenario, given, when, then, parsers



@scenario('smoke_tests.feature', 'Search functionality works')
def test_search_functionality_works():
    pass



@given('I am on the Funda homepage')
def on_homepage(home_page):
    home_page.navigate_to_homepage()
    home_page.verify_page_title()
    home_page.handle_cookie_popup()


@when(parsers.parse('I search for "{city}"'))
def search_for_city( city,home_page):
    home_page.search_for_city(city)
    

@then(parsers.parse('I should see search results for "{city}"'))
def verify_search_results_page(city,search_result_page):
    search_result_page.verify_search_results_page(city)
    


@then('verify listing and pagination are displayed')
def verify_listing_and_pagination(search_result_page):
    search_result_page.verify_properties_are_listed()
    search_result_page.verify_pagination_is_enabled()