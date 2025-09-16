import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

# ---------------------------
# Función de regresión lineal
# ---------------------------
def regresion_lineal(puntos):
    puntos = np.array(puntos)
    X = puntos[:, 0].reshape(-1, 1)
    y = puntos[:, 1]

    modelo = LinearRegression()
    modelo.fit(X, y)

    a = modelo.intercept_
    b = modelo.coef_[0]

    return {
        "tipo": "lineal",
        "a": float(a),
        "b": float(b),
        "ecuacion": f"y = {a:.4f} + {b:.4f}x"
    }

# -------------------------------
# Función de regresión exponencial
# -------------------------------
def regresion_exponencial(puntos):
    puntos = np.array(puntos)
    X = puntos[:, 0]
    y = puntos[:, 1]

    def exp_func(x, a, b):
        return a * np.power(b, x)

    params, _ = curve_fit(exp_func, X, y, p0=(1, 2))
    a, b = params

    return {
        "tipo": "exponencial",
        "a": float(a),
        "b": float(b),
        "ecuacion": f"y = {a:.4f} * ({b:.4f})^x"
    }

# ---------------------------
# Aplicación a los polipastos
# ---------------------------
if __name__ == "__main__":
    # Con pesos intervinientes
    P1 = [( 0 , 1 ),
         ( 1 , 1.81 ),
         ( 2, 4.04 ),
         ( 3 , 6.38 )] # exponencial
    P2 = [( 0 , 1 ),
          ( 3 , 3.48 )] # lineal
    P3 = [( 0 , 1 ),
          ( 3 , 3.76 )] # lineal
    # Sin pesos intervinientes
    P4 = [( 0 , 1 ),
         ( 1 , 1.6 ),
         ( 2, 2.75 ),
         ( 3 , 4.57 )] # exponencial
    P5 = [( 0 , 1 ),
          ( 3 , 2.67 )] # lineal
    P6 = [( 0 , 1 ),
          ( 3 , 2.67 )] # lineal

    # Resultados
    R1, R2, R3, R4, R5, R6 = regresion_exponencial(P1), regresion_lineal(P2), regresion_lineal(P3), regresion_exponencial(P4), regresion_lineal(P5), regresion_lineal(P6)
    # print(R1, R2, R3, R4, R5, R6)
    print(R1["ecuacion"], R2["ecuacion"], R3["ecuacion"], R4["ecuacion"], R5["ecuacion"], R6["ecuacion"], sep="\n")

# -------------------------------
# Resultados (ecuaciones)
# -------------------------------
# (1) ... y = 1.1442 * (1.7846)^x
# (2) ... y = 1.0000 + 0.8267x
# (3) ... y = 1.0000 + 0.9200x
# (4) ... y = 0.9770 * (1.6727)^x
# (5) ... y = 1.0000 + 0.5567x
# (6) ... y = 1.0000 + 0.5567x

