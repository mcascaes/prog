"""
Programação estruturada
2024.1
12/03/2024

ac5
"""
import random

#atributos
def main():
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10,20)
    defesa_aventureiro = random.randint(1,5)
    vida_monstro = random.randint(60,80)
    ataque_monstro = random.randint(20,30)

    print(f"vida do aventureiro : {vida_aventureiro}, ataque do aventureiro : {ataque_aventureiro},defesa do aventureiro:  {defesa_aventureiro} ")
    print(f": vida do monstro :{vida_monstro}, ataque do monstro: {ataque_monstro}")

    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print("Rodada " + str(rodada) + ":")
        dano_aventureiro = random.randint(1, ataque_aventureiro)
        vida_monstro -= dano_aventureiro
        print("O aventureiro ataca o monstro, causando " + str(dano_aventureiro) + " de dano.")

        if vida_monstro <= 0:
            print("O monstro morreu.")
            break

        dano_monstro = random.randint(1, ataque_monstro - defesa_aventureiro)
        vida_aventureiro -= dano_monstro
        print("O monstro ataca o aventureiro, causando " + str(dano_monstro) + " de dano.")

        if vida_aventureiro <= 0:
            print("O aventureiro morreu.")
            break

        rodada += 1
main()