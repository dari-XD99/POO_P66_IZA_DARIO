from controladorS import Controlador
from vistaS import VistaBot

def main():
    controlador = Controlador()
    vista = VistaBot(controlador)
    vista.iniciar()

if __name__ == "__main__":
    main()