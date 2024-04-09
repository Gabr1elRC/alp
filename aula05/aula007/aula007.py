""""""""""
soma = 0
for i in range(1, 6):
    idade = int(input("entre com a idade:"))
    soma = soma + idade
media = soma/5
print(f"a media das idades e {round(media)} anos")

frase = input('digite uma frase : ')
for caracter in frase :
    print(caracter)
"""
qtd = 0
frase = input('digite uma frase :')

for letra in frase:
    if letra in 'aeiouAEIOUÂãÈÉéíÍÓó':
        qtd = qtd + 1
print("a quantidade de vogais  na frase é :",qtd)