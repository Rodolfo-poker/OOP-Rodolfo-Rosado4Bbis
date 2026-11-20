class SuscripcionExpiradaError(Exception):
    """Se lanza al usar una función restringida sin membresía activa."""


class PuntosInsuficientesError(Exception):
    """Se lanza cuando una transacción supera el saldo de gemas."""
