#Pedimos um ano ao usuário
ano = int(input("Informe um ano: "))

#vamos verificar agora se "ANO" é True (bissexto) ou False (nao bissexto)
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

#agora vamos dar o resultado 
print(bissexto)