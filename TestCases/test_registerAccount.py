from Pages.Homepage import HomepageVerification
from Pages.CreateAccount import CreateAccountPage

def test_registerAccount(setup):
    page = setup

    # 1st Verify the landing page.
    homepageTitle = HomepageVerification(page)
    homepageTitle.homepageTitleVerification()

    # Register an Account

    registerAccount = CreateAccountPage(page)
    registerAccount.registerAccount()

