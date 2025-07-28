from M_BE_Led import ModeloLed
from V_BE_Led import VistaLed
from C_BE_Led import ControladorLed

def main():
    modelo = ModeloLed()
    vista = VistaLed()
    controlador = ControladorLed(modelo, vista)
    controlador.ejecutar()

if __name__ == "__main__":
    main()

