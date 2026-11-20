from app_movil import PerfilMovil, PerfilPro


class PerfilController:
    def __init__(self, vista):
        self.vista = vista

    def demo_normal(self):
        perfil = PerfilMovil("ana")
        self.vista.mostrar_perfil(perfil)
        perfil.ganar_gemas(20)
        self.vista.mostrar(f"Tras ganar 20 gemas: {perfil.gemas}")
        try:
            perfil.gastar_gemas(500)
        except Exception as e:
            self.vista.mostrar_error(e)

    def demo_pro(self):
        perfil = PerfilPro("luis", meses_suscripcion=1)
        self.vista.mostrar(perfil.descargar_contenido_offline())
        perfil.consumir_mes()
        try:
            perfil.descargar_contenido_offline()
        except Exception as e:
            self.vista.mostrar_error(e)
        self.vista.mostrar(f"¿Sigue siendo Pro? {perfil.es_pro}")
