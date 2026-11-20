class ConsolaView:
    def mostrar(self, mensaje):
        print(mensaje)

    def mostrar_perfil(self, perfil):
        print(f"Usuario: {perfil.username} | Gemas: {perfil.gemas} | Racha: {perfil.racha_dias} días")

    def mostrar_error(self, error):
        print(f"[ERROR] {error}")
