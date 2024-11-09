import numpy as np
import matplotlib.pyplot as plt

# Constante gravitacional universal
G = 6.67430e-11  # en m^3 kg^-1 s^-2

# Solicitud de parámetros al usuario con validaciones
def obtener_float_positivo(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor <= 0:
                print("El valor debe ser un número positivo.")
            else:
                return valor
        except ValueError:
            print("Por favor, introduce un número válido.")

def obtener_vector_no_cero(prompt_x, prompt_y):
    while True:
        try:
            x = float(input(prompt_x))
            y = float(input(prompt_y))
            if x == 0 and y == 0:
                print("La posición inicial no puede ser (0,0).")
            else:
                return np.array([x, y])
        except ValueError:
            print("Por favor, introduce números válidos para la posición.")

# Solicitar la masa del cuerpo central
M = obtener_float_positivo("Introduce la masa del cuerpo central (en kg): ")  # Masa del cuerpo masivo

# Solicitar la masa del cuerpo orbital, que debe ser menor que la del cuerpo masivo
while True:
    m = obtener_float_positivo("Introduce la masa del cuerpo orbital (en kg): ")
    if m >= M:
        print("La masa del cuerpo orbital debe ser menor que la del cuerpo central.")
    else:
        break

# Solicitar la posición inicial con validaciones
pos_inicial = obtener_vector_no_cero("Introduce la posición inicial X del cuerpo orbital (en metros): ",
                                     "Introduce la posición inicial Y del cuerpo orbital (en metros): ")

# Solicitar la velocidad inicial y el paso de tiempo
vel_inicial = np.array([
    float(input("Introduce la velocidad inicial X del cuerpo orbital (en m/s): ")),
    float(input("Introduce la velocidad inicial Y del cuerpo orbital (en m/s): "))
])
dt = obtener_float_positivo("Introduce el paso de tiempo para la simulación (en segundos): ")

# Configuración de listas para la trayectoria y resultados
trayectoria_x = []
trayectoria_y = []
resultados = []

# Función para calcular la aceleración gravitatoria
def aceleracion_gravitatoria(pos):
    r = np.linalg.norm(pos)  # Distancia al cuerpo masivo
    a_magnitud = -G * M / r**2  # Magnitud de la aceleración gravitatoria
    return a_magnitud * pos / r  # Vector de aceleración

# Método de Runge-Kutta de cuarto orden para la integración
def runge_kutta_4(pos, vel, dt):
    k1_v = aceleracion_gravitatoria(pos) * dt
    k1_x = vel * dt
    k2_v = aceleracion_gravitatoria(pos + k1_x / 2) * dt
    k2_x = (vel + k1_v / 2) * dt
    k3_v = aceleracion_gravitatoria(pos + k2_x / 2) * dt
    k3_x = (vel + k2_v / 2) * dt
    k4_v = aceleracion_gravitatoria(pos + k3_x) * dt
    k4_x = (vel + k3_v) * dt
    vel_nueva = vel + (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
    pos_nueva = pos + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
    return pos_nueva, vel_nueva

# Inicialización de la posición y velocidad
pos = pos_inicial
vel = vel_inicial

# Simulación de la órbita
for i in range(10000):
    trayectoria_x.append(pos[0])
    trayectoria_y.append(pos[1])
    resultados.append((i * dt, pos[0], pos[1], vel[0], vel[1]))
    
    # Actualización de la posición y velocidad usando Runge-Kutta de cuarto orden
    pos, vel = runge_kutta_4(pos, vel, dt)
    
    if np.linalg.norm(pos) > 1e8:
        print("La órbita excede el rango simulado.")
        break

# Impresión de resultados numéricos
print("\nResultados Numéricos de la Simulación:")
print("Tiempo (s)   Posición X (m)   Posición Y (m)   Velocidad X (m/s)   Velocidad Y (m/s)")
for t, x, y, vx, vy in resultados[::100]:
    print(f"{t:>10.2f} {x:>15.2f} {y:>15.2f} {vx:>18.2f} {vy:>18.2f}")

# Visualización de la órbita
plt.figure(figsize=(8, 8))
plt.plot(trayectoria_x, trayectoria_y, label="Órbita")
plt.plot(0, 0, 'ro', label="Cuerpo central (Masa M)")
plt.xlabel("Posición X (m)")
plt.ylabel("Posición Y (m)")
plt.title("Simulación de Órbita en un Campo Gravitatorio")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()