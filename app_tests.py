from app import app
from unittest import TestCase


class BloglyTestCase(TestCase):
    def test_color_form(self):
        with app.test_client() as client:
            res = client.get('/users')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

    def test_redirection(self):
        def test_color_form(self):
            with app.test_client() as client:
                res = client.get('/')

                self.assertEqual(res.status_code, 302)
                self.assertEqual(res.location, 'http://localhost/')

    def test_new_user_form(self):
        def test_color_form(self):
            with app.test_client() as client:
                res = client.get('/create_user', data={'first_name': 'Jack'})
                html = res.get_data(as_text=True)

                self.assertEqual(res.status_code, 200)
