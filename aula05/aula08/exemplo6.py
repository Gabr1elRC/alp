while True:
    idade = input("digite sua idade: ")
    if idade.isdigit():
        idade = int(idade)
        break
    else:
        print("apenas numeros....")