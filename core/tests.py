from django.test import TestCase
from django.contrib.auth.models import User
from polls.models import Session, Question


class FrontendPageTests(TestCase):
    def test_home_page_status_and_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_join_page_status_and_template(self):
        response = self.client.get('/join/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/join.html')

    def test_login_page_status_and_template(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html')

    def test_dashboard_page_status_and_template(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/dashboard.html')

    def test_vote_page_status_and_template(self):
        user = User.objects.create_user(
            username="testhost",
            password="testpass123"
        )

        session = Session.objects.create(
            title="Test Session",
            host=user,
            is_active=True
        )

        Question.objects.create(
            session=session,
            text="Test Question",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D"
        )

        response = self.client.get(f'/vote/{session.code}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/vote.html')