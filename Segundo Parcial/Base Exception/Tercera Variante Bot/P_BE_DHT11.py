from M_BE_DHT11 import ModeloDHT11
from V_BE_DHT11 import VistaDHT11
from C_BE_DHT11 import ControladorDHT11

def main():
    modelo = ModeloDHT11()
    vista = VistaDHT11()
    controlador = ControladorDHT11(modelo, vista)
    vista.iniciar()

if __name__ == "__main__":
    main()