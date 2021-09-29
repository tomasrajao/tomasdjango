from typing import List

from pypro.modulos.models import Modulo


def listar_modulos_ordenados()-> List[Modulo]:
    return list(Modulo.objects.order_by('titulo').all())