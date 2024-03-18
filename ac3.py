#ex1:
def determina_tipo_triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return "Não é um triângulo"
    elif a == b and a == c:
        return "Equilátero"
    elif a ==  b or b == c or a == c:
        return "Isóceles"
    return "Escaleno"

def triangulo_teste():
    while True:
        a = float(input("Digite o comprimento do primeiro lado: "))
        b = float(input("Digite o comprimento do segundo lado: "))
        c = float(input("Digite o comprimento do terceiro lado: "))
        print(determina_tipo_triangulo(a, b, c))
        break

triangulo_teste()


#ex2:
def dia_semana(numero):
    dias_da_semana = {
        1: "domingo",
        2: "segunda-feira",
        3: "terça-feira",
        4: "quarta-feira",
        5: "quinta-feira",
        6: "sexta-feira",
        7: "sábado"
    }
    
    if 1 <= numero <= 7:
        return dias_da_semana[numero]
    else:
        return "número inválido"

def testa_dia_semana():
    
    numero = int(input("Digite o número do dia da semana (1 a 7): "))
    print(dia_semana(numero))


testa_dia_semana()


#ex3:
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

def leitura():
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe outro número: "))
    operacao = input("Informe a operação: ").upper()
    return n1,n2,operacao

def main():
    n1, n2, operacao = leitura()
    match operacao:
        case "SOMA" | "+":
            print(soma(n1, n2))
        case "SUBTRAÇÃO" | "SUBTRACAO" | "-":
            print(subtracao(n1, n2))
        case "MULTIPLICAÇÃO" | "MULTIPLICACAO" | ".":
            print(multiplicacao(n1, n2))
        case "DIVISÃO" | "DIVISAO" | "/":
            print(divisao(n1, n2))
        case _:
            print("Operação inválida")
main()