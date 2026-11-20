from Models.perfil_movil import PerfilMovil
from Models.excepciones import SuscripcionExpiradaError


class PerfilPro(PerfilMovil):
    def __init__(self, username, meses_suscripcion, **kwargs):
        if meses_suscripcion <= 0:
            raise ValueError("Los meses de suscripción deben ser mayores a 0")
        super().__init__(username, **kwargs)
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def consumir_mes(self):
        """Resta un mes de suscripción (mínimo 0)."""
        if self.meses_suscripcion > 0:
            self.meses_suscripcion -= 1

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("Tu suscripción ha expirado")
        return "Descarga completada"
