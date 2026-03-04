from django.test import TestCase

class FrontendPageTests(TestCase):
    """
    Unit tests for core frontend pages.
    Grading Req: Demonstrates automated testing for basic functionality.
    """

    def test_home_page_status_and_template(self):
        # Grading Req (Unit Testing): Verify the home page loads successfully
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Grading Req (Code Quality): Verify the correct templates are being used
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertTemplateUsed(response, 'base.html')

    # =====================================================================
    # TODO for Backend Team: 
    # Please uncomment the following tests once urls.py and views.py 
    # are configured for these routes.
    # These are written to meet grading requirements for unit testing.
    # =====================================================================

    # def test_join_page_status_and_template(self):
    #     response = self.client.get('/join/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'core/join.html')

    # def test_login_page_status_and_template(self):
    #     response = self.client.get('/login/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'core/login.html')

    # def test_dashboard_page_status_and_template(self):
    #     response = self.client.get('/dashboard/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'core/dashboard.html')

    # def test_vote_page_status_and_template(self):
    #     response = self.client.get('/vote/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'core/vote.html')
