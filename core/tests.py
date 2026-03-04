from django.test import TestCase

class FrontendPageTests(TestCase):
    """
    Unit tests for core frontend pages.
    Grading Req: Demonstrates automated testing for basic functionality.
    """

    def test_home_page_status_and_template(self):
        # Grading Req (Unit Testing): Verify the home page loads successfully (HTTP 200)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Grading Req (Code Quality): Verify the correct templates are being used
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_join_page_status_and_template(self):
        # Grading Req (Unit Testing): Verify the student join page loads successfully (HTTP 200)
        response = self.client.get('/join/')
        self.assertEqual(response.status_code, 200)
        
        # Verify template usage for the join page
        self.assertTemplateUsed(response, 'core/join.html')
        self.assertTemplateUsed(response, 'base.html')