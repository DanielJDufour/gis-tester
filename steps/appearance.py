from behave import *
from selenium import webdriver

@given("user has a web browser open")
def open_firefox(context):
    context.driver = webdriver.Firefox()

@given("user has gone to the main page")
@when("user goes to the main page")
def go_to_page(context):
    context.driver.get("http://leafletjs.com/")

@then("page should not be blank")
def check_screenshot(context):
    screenshot = context.driver.get_screenshot_as_base64()

@then("page should not mention errors")
def check_if_error_page(context):
    assert "error" not in context.driver.page_source
    context.driver.quit()

@when("user clicks the zoom-in button")
def click_zoom_in_button(context):
    context.first_screenshot = context.driver.get_screenshot_as_base64()
    context.driver.find_element_by_css_selector("[title='Zoom in']").click()

@then("view should change")
def check_if_view_changed(context):
    second_screenshot = context.driver.get_screenshot_as_base64()
    assert context.first_screenshot != second_screenshot
    context.driver.quit()
