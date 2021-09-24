import pytest
from django.contrib.sites import requests
from django.http import HttpResponse


def test_status_code(client):
    resp = client.get('/')
    assert resp.status_code == 200
