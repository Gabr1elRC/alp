gasolina = 'G-gasolina',
alcool = 'A-alcool',
ltr_gasolina = 2.50
ltr_alcool = 1.90
combustivel = str(input('qual o tipo de combustivel abastecido?'))
litro = int(input("litros vendidos :"))

if combustivel == alcool and litro <= 20:
    total_abastecido = (litro * ltr_alcool)
    desconto = total_abastecido * 0.03
else :
    total_abastecido = (litro * ltr_alcool)
    desconto = total_abastecido * 0.05
if combustivel == gasolina and litro <= 20 :
    total_abastecido = (litro * ltr_gasolina)
    desconto = total_abastecido * 0.04
else :
    total_abastecido = (litro * ltr_gasolina)
    desconto = total_abastecido * 0.06

print(combustivel)
print('o litro de ',combustivel , 'esta :')
print('valor a ser pago :',total_abastecido - desconto)
