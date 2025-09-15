import matplotlib.pyplot as plt
import numpy as np

def calcular_regresion_lineal(datos):
    """
    Calcula la pendiente (w) y la intersección (b) de la línea de regresión
    que minimiza el error cuadrático.
    """
    n = len(datos)
    if n < 2:
        return None, None

    x_coords = [p[0] for p in datos]
    y_coords = [p[1] for p in datos]

    sum_x = sum(x_coords)
    sum_y = sum(y_coords)
    sum_xy = sum(x * y for x, y in datos)
    sum_x2 = sum(x**2 for x in x_coords)

    numerador_w = n * sum_xy - sum_x * sum_y
    denominador_w = n * sum_x2 - sum_x**2
    
    if denominador_w == 0:
        return None, None
        
    w = numerador_w / denominador_w
    
    promedio_x = sum_x / n
    promedio_y = sum_y / n
    b = promedio_y - w * promedio_x
    
    return w, b

def graficar_regresion(titulo, datos, w, b):
    """
    Grafica los puntos originales y la línea de regresión ajustada.
    """
    x_original = [p[0] for p in datos]
    y_original = [p[1] for p in datos]

    x_min = min(x_original) - 1
    x_max = max(x_original) + 1
    x_recta = np.linspace(x_min, x_max, 100)
    y_recta = w * x_recta + b

    #Puntos originales
    plt.figure(figsize=(8, 6))
    plt.scatter(x_original, y_original, color='blue', label='Puntos de Datos', zorder=5)
    
    #Recta calculada con regresion
    plt.plot(x_recta, y_recta, color='red', linestyle='-', label=f'Recta de Regresión: y={w:.2f}x+{b:.2f}')
    
    plt.title(titulo)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig(titulo)
    plt.show()

#Conjunto de datos original
DATOS_ORIGINALES = {(1, 2), (2, 3), (3, 5), (4, 7), (5, 8)}
w1, b1 = calcular_regresion_lineal(DATOS_ORIGINALES)

if w1 is not None:
    print("--- Resultados para el conjunto de datos original ---")
    print(f"Coeficientes w y b: w={w1:.4f}, b={b1:.4f}")
    graficar_regresion("Regresión Lineal con Datos Originales", DATOS_ORIGINALES, w1, b1)
    print("\n")

#Con valores atípicos
# Agregamos un par de puntos extra y un valor atípico
# El punto (10, 1) es un valor atípico, ya que se desvía fuertemente de la tendencia
DATOS_ATIPICOS = DATOS_ORIGINALES.union({(6, 9), (7, 10), (10, 1)})
w2, b2 = calcular_regresion_lineal(DATOS_ATIPICOS)

if w2 is not None:
    print("--- Resultados para el conjunto de datos con valores atípicos ---")
    print(f"Coeficientes w y b: w={w2:.4f}, b={b2:.4f}")
    graficar_regresion("Regresión Lineal con Datos Atípicos", DATOS_ATIPICOS, w2, b2)