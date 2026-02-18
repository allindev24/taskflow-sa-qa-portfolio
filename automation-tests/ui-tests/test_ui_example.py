def test_google_search(page):
    page.goto("https://www.google.com")

    # принять cookies если появится
    if page.locator("button:has-text('Accept')").count() > 0:
        page.locator("button:has-text('Accept')").click()

    page.fill("textarea[name='q']", "Playwright Python")
    page.keyboard.press("Enter")

    page.wait_for_timeout(2000)

    assert "Playwright" in page.title()