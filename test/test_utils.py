import unittest
from datetime import datetime
from nose.tools import raises
import mock
from werkzeug.exceptions import HTTPException
from api.common.utils import get_paginated_list, \
    to_datetime, get_ssm_parameter


class TestUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.endpoint = "/news?start={start}&limit={limit}"
        self.url = "foo/news"
        self.date = '2020-01-01'
        self.invalid_date = '2021-02-29'
        self.ssm_response = {
            'Parameter':
                {
                    'Name': 'fooname',
                    'Value': 'foovalue'
                }
        }

    @raises(HTTPException)
    def test_http_404_error(self):
        get_paginated_list(1, -1, -1, self.url)

    @raises(HTTPException)
    def test_http_204_error(self):
        get_paginated_list(0, -1, -1, self.url)

    def test_empty_prev_url(self):
        links = get_paginated_list(100, 1, 1, self.url)
        prev_url = links.get('prev')
        next_url = links.get('next')
        self.assertIsNone(prev_url)
        self.assertEqual(next_url, self.endpoint.format(limit=1,
                                                        start=2))

    def test_empty_next_url(self):
        links = get_paginated_list(100, 91, 10, self.url)
        prev_url = links.get('prev')
        next_url = links.get('next')
        self.assertIsNone(next_url)
        self.assertEqual(prev_url, self.endpoint.format(limit=90,
                                                        start=81))

    def test_pagination(self):
        links = get_paginated_list(100, 20, 20, self.url)
        prev_url = links.get('prev')
        next_url = links.get('next')
        self.assertEqual(prev_url, self.endpoint.format(limit=19,
                                                        start=1))
        self.assertEqual(next_url, self.endpoint.format(limit=20,
                                                        start=40))

        links = get_paginated_list(1000, 5, 20, self.url)
        prev_url = links.get('prev')
        next_url = links.get('next')
        self.assertEqual(prev_url, self.endpoint.format(limit=4,
                                                        start=1))
        self.assertEqual(next_url, self.endpoint.format(limit=20,
                                                        start=25))

    def test_to_datetime(self):
        date = to_datetime(self.date)
        self.assertEqual(date, datetime(2020, 1, 1))

    @raises(HTTPException)
    def test_to_datetime_404_error(self):
        to_datetime(self.invalid_date)

    @mock.patch('api.common.utils.ssm.get_parameter')
    def test_ssm_parameter(self, mock_parameter):
        mock_parameter.return_value = self.ssm_response
        pwd = get_ssm_parameter('foo')
        self.assertEqual(pwd, 'foovalue')
