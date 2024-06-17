def calcular_anos(populacao_a, populacao_b, taxa_crescimento_a, taxa_crescimento_b):
    anos = 0
    while populacao_a <= populacao_b:
        populacao_a *= (1 + taxa_crescimento_a / 100)
        populacao_b *= (1 + taxa_crescimento_b / 100)
        anos += 1
    return anos

populacao_a = 8000
populacao_b = 200000
taxa_crescimento_a = 3
taxa_crescimento_b = 1.5

anos_necessarios = calcular_anos(populacao_a, populacao_b, taxa_crescimento_a, taxa_crescimento_b)

print("Número de anos necessários para a população do país A ultrapassar a população do país B:", anos_necessarios)
