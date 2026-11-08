import numpy as np

# Crear arrays
a = np.array([1, 2, 3, 4, 5])
b = np.arange(10, 20, 2)  # de 10 a 20 (sin incluir), paso 2

print("Array a:", a)
print("Array b:", b)

# Operaciones vectorizadas (sin necesidad de loops)
print("a * 2:", a * 2)
print("a + b:", a + b)

# Estadísticas básicas
print("Media de a:", np.mean(a))
print("Desviación estándar:", np.std(a))

# Crear una matriz 2D y hacer reshape
matriz = np.arange(12).reshape(3, 4)
print("\nMatriz 3x4:\n", matriz)

# Indexado y slicing
print("Segunda fila:", matriz[1])
print("Columna 2:", matriz[:, 2])

# Álgebra lineal: multiplicación de matrices
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print("\nProducto de matrices:\n", m1 @ m2)