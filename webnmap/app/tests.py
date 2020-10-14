import pytest

from django.test import Client


@pytest.fixture(scope='function')
def client():
    c = Client()
    return c


@pytest.mark.django_db
@pytest.mark.parametrize('url,code', [('', 200),
                                      ('/schedules/', 200),
                                      ('/newscan/', 200),
                                      ('/random_url/', 404)])
def test_routes(client, url, code):
    response = client.get(url)
    assert response.status_code == code
