soma = 0
idade = 100
qtd = 0
while idade !=0:
    idade = int(input(f'idade:{qtd+1}:'))
    if idade != 0:
        soma = soma + idade
        qtd = qtd + 1
media = soma/qtd
print(f"media é:{media}")