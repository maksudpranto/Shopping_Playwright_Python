from Pages.Homepage import HomepageVerification
from Pages.signIn import SignInPage


def test_login(setup):
    page = setup

    homePageVerify = HomepageVerification(page)
    homePageVerify.homepageTitleVerification()

    login = SignInPage(page)
    login.login()




