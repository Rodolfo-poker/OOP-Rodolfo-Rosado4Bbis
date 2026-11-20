from Views.consola_view import ConsolaView
from Controller.perfil_controller import PerfilController

if __name__ == "__main__":
    controlador = PerfilController(ConsolaView())
    controlador.demo_normal()
    print("-" * 30)
    controlador.demo_pro()
