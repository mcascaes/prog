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
print("R$"(salario_final))
