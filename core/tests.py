from django.test import TestCase

class PageLoadTests(TestCase):
    """Tests to ensure core pages load correctly (Status Code 200)"""
    
    def test_home_page_status(self):
        """Verify that the landing page is accessible"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_join_page_status(self):
        """Verify that the student join page (M3) is accessible"""
        response = self.client.get("/join/")
        self.assertEqual(response.status_code, 200)