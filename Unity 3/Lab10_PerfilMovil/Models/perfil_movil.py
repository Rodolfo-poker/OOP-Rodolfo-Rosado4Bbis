from Models.excepciones import PuntosInsuficientesError


class PerfilMovil:
    def __init__(self, username, gemas=50, racha_dias=1, notificaciones_activas=True):
        if gemas < 0:
            raise ValueError("Las gemas no pueden ser negativas")
        self.username = username
        self._gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    @property
    def gemas(self):
        return self._gemas

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._gemas += cantidad
        return self._gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self._gemas:
            raise PuntosInsuficientesError("No tienes gemas suficientes")
        self._gemas -= cantidad
        return self._gemas
