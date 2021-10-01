import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aulas(modulo):
    return baker.make(Aula, 3, modulo=modulo)


@pytest.fixture
def resp(client, modulo, aulas):
    return client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_titulos_aulas(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_link_aulas(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())


def test_breadcrumb_modulos(resp, modulo: Modulo):
    assert_contains(resp, f'li class="breadcrumb-item active" aria-current="page">{modulo.titulo}')


def test_breadcrumb_link(resp):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{reverse("modulos:indice")}')
