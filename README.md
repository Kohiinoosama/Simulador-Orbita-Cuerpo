# Simulador-Orbita-Cuerpo
Simulador de la órbita de un cuerpo bajo un campo gravitacional
# Simulador de Órbita de un Cuerpo en un Campo Gravitatorio

Este es un simulador en Python que calcula y visualiza la órbita de un cuerpo en torno a un cuerpo masivo, bajo la influencia de la gravedad. El simulador utiliza las leyes de Kepler y la ley de gravitación universal de Newton para determinar cómo se desplaza el cuerpo orbital en un sistema de referencia 2D.

## Características

- Cálculo y simulación de órbitas en 2D.
- Implementación de las leyes de Kepler y la ley de gravitación de Newton.
- Visualización interactiva de las órbitas utilizando Matplotlib.
- Permite variar los parámetros de las simulaciones como la masa del cuerpo central, la masa del objeto orbital, y la velocidad inicial.

## Instalación

### Requisitos previos:

- Python 3.x o superior.
- Librerías de Python:
  - `numpy`
  - `matplotlib`

### Para instalar las librerías necesarias:

Puedes instalar las dependencias utilizando `pip`:

### Introducir parámetros:

El programa pedirá que ingreses los siguientes parámetros para realizar la simulación:

- Masa del cuerpo central (por ejemplo, una estrella o un planeta).
- Masa del objeto orbital (un satélite o planeta).
- Posición inicial del objeto orbital (en el eje X e Y).
- Velocidad inicial del objeto orbital.
- Tiempo en segundos.

  Se aconsejan valores con cierto sentido para que la simulación se dibuje correctamente, por ejemplo:
  - Masa del cuerpo central (5.972e24)
  - masa del cuerpo orbital (1)
  - posición inicial X (7.0e6)
  - posición inicial Y (0)
  - Velocidad X (0)
  - Velocidad Y (7500)
  - Tiempo (60)

Visualización:

El programa mostrará la trayectoria de la órbita en un gráfico 2D, utilizando MatPlotlib.
El código usa la ley de gravitación universal de Newton, así como el método Runge-Kutta de orden 4 para resolver las ecuaciones del movimiento.

