from typing import List

import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aulas.extend(baker.make(Aula, 3, modulo=modulo))
    return aulas


@pytest.fixture
def resp(client, modulos, aulas):
    return client.get(reverse('modulos:indice'))


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_indice_modulos(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_indice_aulas(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_indice_link_aulas(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
