nome = input('digite seu nome: ')
nascimento = input('digite a data nsc <dd/mm/aaaa>:')
data = nascimento.split('/')
palavra = nome.split()
pre_nome = palavra[0]
sobrenome = palavra[1]

print(f'ola {pre_nome}... Muito bonito seu sobrenome: {sobrenome}')
print(f'Voce nasceu no dia {data[0]} e no mes {data[1]} no ano de {data[2]}')