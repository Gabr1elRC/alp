
def ordenar_decrescente(num1, num2, num3):
    lista_numeros = [num1, num2, num3]
    lista_numeros.sort(reverse=True)
    return lista_numeros


def main():
    # Ler os números do usuário
    num1 = int(input("Digite o 1° número: "))
    num2 = int(input("Digite o  2° numero: "))
    num3 = int(input("Digite o 3° número: "))


    numeros_ordenados = ordenar_decrescente(num1, num2, num3)


    print("Números em ordem decrescente:", numeros_ordenados)


if __name__ == "__main__":
    main()




