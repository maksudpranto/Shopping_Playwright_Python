import pytest

@pytest.fixture()
def setup(page):
    page.goto("https://magento.softwaretestingboard.com/")
    yield page


