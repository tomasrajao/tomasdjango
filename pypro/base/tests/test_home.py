import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')


def test_lorem_ipsum(resp):
    assert_not_contains(resp, 'Lorem ipsum')


def test_link_modulo(resp):
    assert_contains(resp, f'href="{reverse("modulos:indice")}"')
