with open("usuarios.txt", "r",) as arquivo:
    linhas = arquivoEntrada.readLines()


usuarios = []
esparcosUtilizados =[]
espacoTotal = 0.0
for linha in linhas:
    campos = linha.split()
    usuario = campos[0]
    espacoUtilizado = int(campos[1])
    usuarios.append(usuario)
    espacoUtilizado.append(espacoUtilizado)
    