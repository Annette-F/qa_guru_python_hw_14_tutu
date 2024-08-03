import pytest

from selene import browser

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def setting_browser():
    browser.config.base_url = 'https://www.tutu.ru'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)


    browser.quit()