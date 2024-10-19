class CreateAccountPage:
    def __init__(self,page):
        self.page = page

        # Register Locators
        self._registerCTA = page.get_by_role("link", name="Create an Account")
        self._firstName = page.get_by_label("First Name")
        self._lastName = page.get_by_label("Last Name")
        self._email = page.get_by_label("Email", exact=True)
        self._password = page.get_by_role("textbox", name="Password*", exact=True)
        self._confirmPassword = page.get_by_label("Confirm Password")
        self._submitCTA = page.get_by_role("button", name="Create an Account")


    def registerAccount(self):
        self._registerCTA.click()
        self._firstName.fill("Md Maksud Hossain")
        self._lastName.fill("Pranto")
        self._email.fill("pranto@gmail.com")
        self._password.fill("Pranto009#")
        self._confirmPassword.fill("Pranto009#")
        self._submitCTA.click()

