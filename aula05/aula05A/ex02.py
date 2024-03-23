print('Calculando a media dos alunos')
nota1 = float(input('digite a primeira nota '))
nota2 = float(input('digite a segunda nota'))
media = (nota1 + nota2)/2
if media >= 9.0:
   aproveitamento = 'A'
elif media >= 7.5 :
    aproveitamento = 'B'
elif media >= 6.0 :
    aproveitamento = 'C'
elif media >= 4.0:
    aproveitamnto = 'D'
else :
    aproveitamento = 'E'


print('media :',media,'     aproveitamento :',aproveitamento)
if media >= 6.0 :
    print('voce foi aprovado')
else :
    print('voce foi reprovado')
