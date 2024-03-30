from tests.base_test import BaseTest
from test_data.newsletter_test_data import EmailData
from time import sleep


class NewsletterTest(BaseTest):
    """
    Entering incorrect email in newsletter box TEST
    """
    def setUp(self):
        super().setUp()
        self.test_data = EmailData()

    def test_wrong_email_entered(self):
        # STEPS
        # 1. Information about commencing the test
        print("Start of the newsletter test: test_wrong_email_entered")
        # 2. Disable cookies
        self.home_page.cookie_button_click()
        # 3. Find newsletter box and enter incorrect email
        self.email_field = self.home_page.enter_email(self.test_data.bad_email)
        # 4. Click on submit button
        self.home_page.click_submit_email_btn()
        # 5. Check if correct message is displayed
        self.assertEqual('Newsletter : Nieprawidłowy adres e-mail', self.home_page.get_user_error_message())
        sleep(3)
        # 6. Information about the end of the test
        print("End of the newsletter test: test_wrong_email_entered")
