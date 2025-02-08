from pytest_bdd import scenario , given, when, then


@scenario('smoke_tests.feature', 'Homepage loads successfully')
def test_homepage_loads_successfully():
    pass



@given('I navigate to the Funda homepage')
def navigate_to_homepage(home_page):
    home_page.navigate_to_homepage()
    home_page.verify_page_title()



@then('the homepage should load successfully')
def homepage_loads_successfully(home_page):
    home_page.handle_cookie_popup()
    home_page.verify_search_box_is_visible()