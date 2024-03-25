valor_compra = float(input('digite o valor da compra :'))
if valor_compra <= 1000.00:
    desconto = valor_compra * 0.10
elif valor_compra <= 5000.00:
    desconto = valor_compra * 0.20
else:
    desconto = valor_compra * 0.30

print('valor da compra :', valor_compra)
print('desconto:', desconto)
print('valor total da compra :',valor_compra - desconto)