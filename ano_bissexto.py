ano = int(input("Digite um ano entre 2000 e 4000 : "))
if ano > 2000 and ano < 4000:
    bissexto = (ano - 2000) // 4
    print("Desde o ano 2000 até o ano ",ano ," tiveram ", bissexto, " anos bissextos")
else :
    print("Ano inválido")
