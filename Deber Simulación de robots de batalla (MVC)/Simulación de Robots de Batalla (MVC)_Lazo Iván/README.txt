Deber de POO66: Simulación de Robots de Batalla (MVC)
Nombre: Iván Lazo


Descripción
Este proyecto implementa una simulación de combate entre robots utilizando Modelo-Vista-Controlador (MVC). Los robots se enfrentan en un torneo de cuarto de finales.

Cambios Realizados:

1.- Modelo (robot_modelo.py):

Se agregó un escudo, que reduce el daño recibido en un porcentaje aleatorio entre 10% y 40%.

Además, se incluyo habilidad especial usar_habilidad(), que permite a cada robot curarse 25 puntos de energía una vez por torneo.

Y para el reporte se añadieron atributos danio_infligido y danio_recibido.

2. Vista (robot_vista.py):

Se agregó la función mostrar_reporte_final() este se muestra al final y enseña los siguientes parametros:

-El ganador del torneo

-Rondas jugadas

-Energía restante

Daños infligidos y recibidos por cada robot

3. Controlador (robot_controlador.py):

Se creó un torneo de eliminación el cual tiene tres jugadas 2 semifinales y una final con 4 robots, cada pelea es aleatoria:

-AlphaX

-OmegaZ

-Atom

-Wall-e


Cada robot utiliza su habilidad si su energía baja a 30 puntos.
