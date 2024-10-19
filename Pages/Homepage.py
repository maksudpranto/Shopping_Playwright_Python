class HomepageVerification:
    def __init__(self, page):
        self.page = page

    def homepageTitleVerification(self):
        actual_title = self.page.title()
        expected_title = "Home Page"

        assert actual_title == expected_title
