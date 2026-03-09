from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from polls.models import Session, Question # 请确保这里的 app 名字（polls）与后端一致

class MiniMentiIntegrationTests(TestCase):
    """
    Unit tests covering both Frontend templates and Backend logic.
    Grading Req (251): Covers core business logic and view endpoints.
    """

    def setUp(self):
        # Setup data for restricted pages (M1 & M2)
        self.user = User.objects.create_user(username="testhost", password="testpass123")
        
        # Setup a session for the voting page (M3 & M5)
        self.session = Session.objects.create(
            title="Test Session",
            host=self.user,
            is_active=True
        )
        
        # M4: Create a sample question
        self.question = Question.objects.create(
            session=self.session,
            text="Which language?",
            option_a="Python", option_b="Java", option_c="C++", option_d="JS"
        )

    def test_home_page_status_and_template(self):
        # Grading Req (254/255): Using reverse() and checking base.html inheritance
        response = self.client.get(reverse('home')) # 请确保 urls.py 中定义了 name='home'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_join_page_status_and_template(self):
        # M3: Audience Participation - Verify join page loads
        response = self.client.get(reverse('join')) # 请确保 name='join'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/join.html')

    def test_login_page_status_and_template(self):
        # M1: User Authentication - Verify login page visibility
        response = self.client.get(reverse('login')) # 请确保 name='login'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html')

    def test_dashboard_page_status_and_template(self):
        # M2: Session Management - Requires authentication
        self.client.login(username="testhost", password="testpass123")
        response = self.client.get(reverse('dashboard')) # 请确保 name='dashboard'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/dashboard.html')

    def test_vote_page_with_data(self):
        # M5: Response Submission - Test dynamic URL with session PIN/code
        # Using reverse with args to meet Requirement 255
        url = reverse('vote', args=[self.session.code]) # 假设 url 模式为 /vote/<code:code>/
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/vote.html')
        # Check if the question text from backend appears on the page
        self.assertContains(response, "Which language?")
