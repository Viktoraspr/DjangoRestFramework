from django.test import TestCase


class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_testroompage(self):
        response = self.client.get('/rooms/')
        self.assertEqual(response.status_code, 200)

    def test_testreservationpage(self):
        response = self.client.get('/reservations/')
        self.assertEqual(response.status_code, 200)
