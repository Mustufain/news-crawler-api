import unittest
from api.app import app


class Base(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()


class TestNewsApi(Base):

    def test_get_news(self):
        response = self.app.get('/news')
        json_response = response.get_json()
        self.assertEqual(json_response['_links']['start'], 1)
        self.assertEqual(json_response['_links']['limit'], 20)
        self.assertEqual(json_response['_links']['next'],
                         '/news?start=21&limit=20')
        self.assertIsNone(json_response['_links'].get('prev'))
        self.assertEqual(response.status_code, 200)

    def test_get_news_404(self):
        response = self.app.get('/news?start=-1')
        self.assertEqual(response.status_code, 404)


class TestSearchNewsPostedDateApi(Base):

    def test_get_news(self):
        response = self.app.get('/news/2021-03-11')
        self.assertEqual(response.status_code, 200)

    def test_get_news_404(self):
        response = self.app.get('/news/2021-02-29')
        self.assertEqual(response.status_code, 404)

    def test_get_news_invalid_format(self):
        response = self.app.get('/news/02-09-2021')
        self.assertEqual(response.status_code, 404)
