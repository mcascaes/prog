def ler_nome():
    nome = input("Informe seu nome: ")
    if nome == "":
        print("Nome inválido. Por favor, informe um nome válido.")
        return ler_nome()
    return nome


def ler_notas():
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    asub = float(input("Informe a nota da AS: "))
    ac = float(input("Informe a nota da AC: "))

    return ap1, ap2, asub, ac

def validar_notas(ap1, ap2, asub, ac):
    if 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10:
        return True
    else:
        print("Nota inválida , encerrando.")
        exit()

def duas_maiores_notas(ap1, ap2, asub):
    if ap1 >= ap2 and ap1 >= asub:
        if ap2 >= asub:
            return ap1, ap2
        else:
            return ap1, asub
    elif ap2 >= ap1 and ap2 >= asub:
        if ap1 >= asub:
            return ap2, ap1
        else:
            return ap2, asub
    else:
        if ap1 >= ap2:
            return asub, ap1
        else:
            return asub, ap2

def calcular_media(n1, n2, ac):
    media = (n1 + n2) * 0.4 + ac * 0.2
    return media

def informar_aprovacao(media):
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Você foi aprovado!")
    else:
        print("Você foi reprovado!")

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)

main()