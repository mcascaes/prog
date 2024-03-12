# Função para resolver a equação de segundo grau
def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta >= 0:
        sqrt_delta = delta**0.5
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        return x1, x2
    else:
        return "Raízes inválidas"

# Obter coeficientes do usuário
a = float(input("Digite o coeficiente 'a' da equação de segundo grau: "))
b = float(input("Digite o coeficiente 'b' da equação de segundo grau: "))
c = float(input("Digite o coeficiente 'c' da equação de segundo grau: "))

# Calcular e imprimir as raízes
raizes = eq_seg_grau(a, b, c)
print("As raízes da equação são:", raizes)



# Ano bissexto

ano = int(input("Digite um ano: "))

def bissexto(ano):
    # Verifica se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

bissexto_resultado = bissexto(ano)

if bissexto_resultado:
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    salario_bruto = float(valor_hora) * float(num_horas)
    desconto_irpf = salario_bruto * irpf
    salario_liquido = salario_bruto - desconto_irpf
    return salario_liquido

# Solicitação do usuário
valor_hora = input("Informe o valor da hora: ")
num_horas = input("Informe o número de horas: ")

# Chama a função e exibe o resultado
salario_final = calcula_salario(valor_hora, num_horas)
print("R$", salario_final)  
