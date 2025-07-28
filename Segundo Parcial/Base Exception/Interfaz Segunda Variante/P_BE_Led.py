from M_BE_Led import ModeloLed
from V_GUI_BE_Led import VistaLedGUI
from C_BE_Led import ControladorLed

def main():
    modelo = ModeloLed()
    
    # Creamos una vista con un controlador temporal
    vista = VistaLedGUI()  # Sin pasar el controlador aún
    
    controlador = ControladorLed(modelo, vista)
    
    # Ahora sí, asignamos el controlador correctamente
    vista.set_controlador(controlador)

    vista.iniciar()

if __name__ == "__main__":
    main()
