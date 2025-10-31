# IA simple para predecir órbita de satélite
import numpy as np
import matplotlib.pyplot as plt

# Datos falsos de ejemplo (posición en km)
t = np.linspace(0, 100, 100)  # tiempo
x = 7000 * np.cos(0.001 * t)  # órbita circular
y = 7000 * np.sin(0.001 * t)

plt.plot(x, y)
plt.title("Órbita simulada de satélite")
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.axis('equal')
plt.show()

Add orbit prediction script
