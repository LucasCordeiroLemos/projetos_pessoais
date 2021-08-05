import random


def executa():
    
    print("Rolador de Dados".upper())

    while True:

        lados = int(input("\nEscolha seu dado (escreva o número de lados): "))

        quantidade = int(input("\nRolando d{}. Quantos dados?\n".format(lados)))

        for n in range(0, quantidade):
            rola_dado(lados)


def rola_dado(lados):
    rolagem = random.randrange(1, lados + 1)
    print("Rolando: d{}; Resultado: {}".format(lados, rolagem))


if __name__ == "__main__":
    executa()
