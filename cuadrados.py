import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

# Calcular los valores necesarios para la regresión
n = len(X)  # Número de datos
sumX = np.sum(X)
sumY = np.sum(Y)
sumX2 = np.sum(X**2)
sumXY = np.sum(X * Y)

# Calcular los coeficientes de la regresión
a = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX**2)
b = (sumY - a * sumX) / n

# Calcular los valores ajustados (Y_pred) usando la ecuación de la línea de regresión
Y_pred = a * X + b

# Visualizar los datos y la línea de regresión
plt.scatter(X, Y, label='Datos reales')
plt.plot(X, Y_pred, color='red', label='Regresión lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Imprimir los coeficientes de la regresión
print(f"Coeficiente a (pendiente): {a}")
print(f"Coeficiente b (intersección): {b}")
