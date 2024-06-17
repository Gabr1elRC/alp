print("digite um os tres lados do triangulo")
a = int(input("digite o primeiro lado do triangulo : "))
b = int(input("digite o segundo lado do triangulo:"))
c = int(input("digite o terceiro lado do triangulo:"))

if (a+b<c) and (a+c<b) and (b+c<a):
    print("isso é um tringulo")
    if (a == b) and (a == c):
        print("é um triangulo equilatero")
    elif (a == b ) or (a == c ) or (c == b ):
        print("é um triangulo isoceles ")
    elif(a != b ) and (b != c ):
        print("é um triangulo escaleno")
else:
    print("isso não é um triangulo ")