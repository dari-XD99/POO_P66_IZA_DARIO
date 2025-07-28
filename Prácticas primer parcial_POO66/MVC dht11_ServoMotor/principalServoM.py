from controladorServoM import Controlador
from vistaServoM import VistaBot

def main():
    controlador = Controlador()
    vista_bot = VistaBot(controlador)
    vista_bot.iniciar()

if __name__ == "__main__":
    main()
