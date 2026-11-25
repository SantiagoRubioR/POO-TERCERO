from modelo import ListaMedicamentos
from vista import VistaFarmacia
from controlador import ControladorFarmacia

modelo = ListaMedicamentos()
vista = VistaFarmacia()
controlador = ControladorFarmacia(modelo, vista)

controlador.iniciar()