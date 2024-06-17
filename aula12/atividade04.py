from math import pi, pow
def esfera(raio):
    return (3/4)*pi*pow(raio, 3)

r = float(input("digite o raio "))
print(f"o volume da esfera de raio {r} é {esfera(r)}:")
