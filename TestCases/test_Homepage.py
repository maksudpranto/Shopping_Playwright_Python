from Pages.Homepage import HomepageVerification

def test_HomepageVerification(setup):
    page = setup

    titleVerification = HomepageVerification(page)
    titleVerification.homepageTitleVerification()
