import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def graficar(grupos, rango_x=(-10, 10), rango_y=None, puntos=400):
    """
    Grafica varios grupos de funciones.

    Parámetros:
    - grupos: lista de listas con funciones como tuplas (nombre, expresión).
              Ej: [[("Cuadrática", "x**2"), ("Seno", "np.sin(x)")]]
    - rango_x: tupla (min, max) para X
    - rango_y: tupla (min, max) para Y (opcional)
    - puntos: número de puntos en el rango
    """
    x = np.linspace(rango_x[0], rango_x[1], puntos)

    # Creamos subplots: uno por grupo
    fig, axs = plt.subplots(len(grupos), 1, figsize=(8, 4*len(grupos)))

    # Si solo hay 1 grupo, axs no es lista → lo convertimos
    if len(grupos) == 1:
        axs = [axs]

    for i, funciones in enumerate(grupos):
        for nombre, expr in funciones:
            try:
                y = eval(expr)
                axs[i].plot(x, y, label=nombre)
            except Exception as e:
                print(f"Error en la función {expr}: {e}")
        axs[i].set_title(f"Gráfico {i+1}")
        axs[i].grid(True)
        axs[i].axhline(0, color="black", linewidth=0.5)
        axs[i].axvline(0, color="black", linewidth=0.5)
        if rango_y:
            axs[i].set_ylim(rango_y)  # Limite en eje Y
        axs[i].legend()

    plt.tight_layout()
    plt.show()

g1 = ("Potencial ideal", "2**x")
g2 = ("Factorial ideal", "2*x")
g3 = ("Potencial real (con p.i.)", "1.1442 * (1.7846**x)")
g4 = ("Factorial horizontal real (con p.i.)", "1.0000 + 0.8267*x")
g5 = ("Factorial vertical real (con p.i.)", "1.0000 + 0.9200*x")
g6 = ("Potencial real (sin p.i.)", "0.9770 * (1.6727**x)")
g7 = ("Factorial horizontal real (sin p.i.)", "1.0000 + 0.5567*x")
g8 = ("Factorial vertical real (sin p.i.)", "1.0000 + 0.5567*x")


grupos = [
    [g1, g2],
    [g3, g4, g5],
    [g6, g7, g8],
    [g1, g3, g6],
    [g2, g4, g7],
    [g2, g5, g8]
]

graficar(grupos, rango_x=(0, 6))
