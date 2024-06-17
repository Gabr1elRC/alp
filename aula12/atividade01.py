def epar(n):
    if n%2 == 0:
        return True
    return False
x = int(input("digite um valor :"))

if epar(x):
    print("o valor digitado é par")
else:
    print("o valor digitado é impar")