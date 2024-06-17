frase = input('digite uma frase: ').strip()
palavras = frase.split()
frase1 = ''
for palavra in palavras:
    frase1 = frase1 + palavra
    frase2 = frase1[::-1]
if frase1 == frase2:
    palindromo = True
else:
    palindromo = False
if palindromo:
    print('é um palindromo')
else:
    print('nao é um palindromo!')

