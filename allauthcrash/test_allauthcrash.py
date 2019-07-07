import pytest
from django.test import Client


@pytest.mark.django_db
def test_signup_get():
    client = Client()
    resp = client.get('/accounts/login/')
    assert 'Google' in resp.content.decode()

