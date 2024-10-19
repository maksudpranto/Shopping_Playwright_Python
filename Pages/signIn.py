class SignInPage():
    def __init__(self, page):
        self.page = page
        self._signInButton = page.locator("//div[@class='panel header']//a[contains(text(),'Sign In')]")
        self._emailField = page.locator("//input[@id='email']")
        self._passwordField = page.locator("(//input[@id='pass'])")
        self._LoginButton = page.locator("//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")


    def login(self):
        self._signInButton.click()
        self._emailField.fill("pranto@gmail.com")
        self._passwordField.fill("Pranto009#")
        self._LoginButton.click()






