salarioHora = float(input('qual o seu salario/hora ?'))
horasMes = int(input('digite o total de horas trabalhadas no mes?'))
salarioBruto = salarioHora * horasMes
if salarioBruto <= 900:
        ir = 0
        aliquota = 0
elif salarioBruto <= 1500:
        ir = salarioBruto * 0.05
        aliquota = 5
elif salarioBruto <= 2500:
        ir = salarioBruto * 0.10
        aliquota =10
else :
        salarioBruto * 0.20
        aliquota =20

inss = salarioBruto * 0.10
fgts = salarioBruto * 0.11
impostoSindicato = salarioBruto * 0.03
total_Descontos = ir + inss
salarioLiquido = salarioBruto - total_Descontos

print('salario bruto:(',salarioHora * horasMes,')  :  R$',salarioBruto)
print('(-) IR (',aliquota,'%)  : R$',ir)
print('(-) INSS (10%)  :  R$',inss)
print('fgts (11%)  :  R$',fgts)
print('Total de descontos :  R$',total_Descontos)
print('salario liquido  :   R$',salarioBruto - total_Descontos)






