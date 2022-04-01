import random
pontos = 1000

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print(numero_secreto)
print("Qual o nivél da dificuldade")
print("(1) Facíl, (2) Médio, (3) Dificíl")
nivel = int(input("Defina o nivél de dificuldade:"))

if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 5
else:
    total_de_tentativas = 3




for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou " , chute)
    

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você fez {}".format(pontos))
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")