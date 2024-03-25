largura = float(input('digite a largura da parede :'))
comprimento = float(input('digite o comprimento da parede:'))
ltr_lata = float(input('digite a quantidade de litros por lata de tinta :'))
rendimento_lata = float(input("digite o rendimento por litro da lata : "))
porta_alt = float(input('digite a altura da porta : '))
porta_comp = float(input('digite o comprimento da porta :'))
porta = porta_alt * porta_comp
quarto = (comprimento * largura)*4
quarto_porta = quarto - porta
lata = ltr_lata * quarto_porta
qtd_lata = rendimento_lata/ltr_lata
print('sera necessario compra :',lata ,'litros de tinta')
print('sera necessario :',qtd_lata,'de latas de tinta ')

