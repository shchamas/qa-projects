# Project 4: SauceDemo Automation with Playwright + Python
# Automates Manual Project 1 - Login Tests

from playwright.sync_api import Page, expect
import pytest

URL = "https://www.saucedemo.com"

def login(page: Page, username, password):
    page.goto(URL)
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")

def test_1_valid_login(page: Page):
    # Manual Test 1 - Valid login should go to inventory page
    login(page, "standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

def test_2_invalid_password(page: Page):
    # Manual Test 2 - Wrong password should show error
    login(page, "standard_user", "wrong_password")
    expect(page.locator("[data-test='error']")).to_contain_text("Username and password do not match")

def test_3_locked_user(page: Page):
    # Manual Test 3 - Locked out user should be blocked
    login(page, "locked_out_user", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("Sorry, this user has been locked out")

def test_4_empty_login(page: Page):
    # Manual Test 4 - Empty fields should show error
    login(page, "", "")
    expect(page.locator("[data-test='error']")).to_contain_text("Username is required")
