import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.arange(10, 20, 2)

print("Array a:", a)
print("Array b:", b)

print("a * 2:", a * 2)
print("a + b:", a + b)

print("Media de a:", np.mean(a))
print("Desviación estándar:", np.std(a))

matriz = np.arange(12).reshape(3, 4)
print("\nMatriz 3x4:\n", matriz)

print("Segunda fila:", matriz[1])
print("Columna 2:", matriz[:, 2])

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print("\nProducto de matrices:\n", m1 @ m2)
