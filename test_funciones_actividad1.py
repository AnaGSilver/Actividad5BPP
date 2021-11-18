import pytest
import Actividad_leccion1_A_funciones as af

def test_minimo():
    l1 = [1, 2, 3, 4, 10, -100]
    l2 = [3, 8, 40, 10, 9]
    assert af.minimo(l1) == -100
    assert af.minimo(l2) == 3


def test_maximo():
    l1 = [-1, 2, 3000, 4, 45, 100]
    l2 = [3, 778, 490, 10, 1000]
    assert af.maximo(l1) == 3000
    assert af.maximo(l2) == 1000


def test_media():
    l1 = [2, 2, 2, 2, 2, 2, 2, 2]
    l2 = [6, 8, 6, 8, 6, 8, 6, 8]
    assert af.media(l1) == 2
    assert af.media(l2) == 7
