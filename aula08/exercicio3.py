'''
v = 0
frase = input('digite uma palavra :')
for letra in frase:
    if letra.lower() in "aeiou":
        v = v + 1

print(f'a frase tem {v}vogal(is).')
'''
v = 0
frase = input('digite uma frase').lower()
for vogal in "aeiou":
    v = v + frase.count(vogal)

print(f'a frase tem {v}vogal(is).')