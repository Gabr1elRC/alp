'''
data = input('digite o ano d seu nascimento <dd/mm/aaaa> :')
dia = data[0:2]
mes =data[3:5]
ano =data[6:10]
data_invertida = ano+mes+dia

print(data," - ", data_invertida)
'''

data = input('digite uma data:')
info = data.split('/')
dia = info[0]
mes = info[1]
ano = info[2]
data_invertida = ano+mes+dia

print(data," - ", data_invertida)
