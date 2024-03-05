def calcular_o_delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

delta = calcular_o_delta


#Pedir os parâmetros para o usuario
a = float(input("Informe o parâmetro a da equação "))
b = float(input("Informe o parâmetro b da equação "))
c = float(input("Informe o parâmetro c da equação "))


#Calcular a primeira raiz
raiz1_x = (-b + delta(a, b, c)**0.5) / (2*a)

#Resposta da primeira raiz
print("A primeira raiz da equação é: ", raiz1_x)

#Calcular a segunda raiz
raiz2_x = (-b - delta(a, b, c)**0.5) / (2*a)

#Resposta da segunda raiz
print("A segunda raiz da equação é ",raiz2_x)