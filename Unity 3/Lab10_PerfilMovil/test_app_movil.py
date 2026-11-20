import pytest
from app_movil import (
    PerfilMovil, PerfilPro,
    SuscripcionExpiradaError, PuntosInsuficientesError,
)


# 1. Fixture
@pytest.fixture
def perfil():
    return PerfilMovil("ana")


# 2. Integridad estructural y aserciones
def test_valores_iniciales(perfil):
    assert perfil.username == "ana"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_ganar_gemas(perfil):
    assert perfil.ganar_gemas(10) == 60


def test_gastar_gemas(perfil):
    assert perfil.gastar_gemas(20) == 30


def test_consistencia_aritmetica(perfil):
    perfil.ganar_gemas(30)
    perfil.gastar_gemas(10)
    assert perfil.gemas == 70


# 3. Excepciones
def test_gemas_iniciales_negativas():
    with pytest.raises(ValueError):
        PerfilMovil("x", gemas=-5)


def test_gastar_mas_de_lo_disponible(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(100)


def test_gastar_cantidad_invalida(perfil):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(0)


def test_pro_meses_invalidos():
    with pytest.raises(ValueError):
        PerfilPro("luis", meses_suscripcion=0)


def test_descarga_con_suscripcion_expirada():
    pro = PerfilPro("luis", meses_suscripcion=1)
    pro.consumir_mes()
    with pytest.raises(SuscripcionExpiradaError):
        pro.descargar_contenido_offline()
    assert pro.es_pro is False


# 4. Parametrizados
@pytest.mark.parametrize("cantidad, esperado", [
    (1, 51),
    (10, 60),
    (100, 150),
])
def test_ganar_gemas_validas(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -1, -50])
def test_ganar_gemas_invalidas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)


# 5. Tipo y jerarquía
def test_herencia():
    pro = PerfilPro("luis", meses_suscripcion=3)
    assert isinstance(pro, PerfilMovil)
    assert isinstance(pro, PerfilPro)


def test_ciclo_de_vida_pro():
    pro = PerfilPro("luis", meses_suscripcion=1)
    assert pro.es_pro is True
    assert pro.descargar_contenido_offline() == "Descarga completada"
    pro.consumir_mes()
    with pytest.raises(SuscripcionExpiradaError):
        pro.descargar_contenido_offline()
    assert pro.es_pro is False
