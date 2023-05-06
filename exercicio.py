import random


print('***************')
print('Bem vindo ao jogo')
print('***************')

numero_premiado = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Escolha o nivel: ")
print("(1)Fácil (2)Médio (3)Dificil")
nivel = int(input("Escolha o nivel: "))


if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
    
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input('Chute um numero: ')
    print("Voce digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("\nVoce deve digitar um numero de 1 a 100")
        continue

    acertou = chute == numero_premiado
    maior = chute > numero_premiado
    menor = chute < numero_premiado
    

    if (acertou):
        print("\nVocê acertou! Você fez {}".format(pontos))
        break
    else:
        pontos_perdidos = abs(numero_premiado - chute)
        pontos = pontos - pontos_perdidos
        if maior:
            print("\nO seu chute foi maior que o numero premiado")
            if rodada == total_de_tentativas:
                print("\nVoce perdeu, o numero era: {}".format(numero_premiado))
                print("Você fez {} pontos".format(pontos))
        elif menor:
            print("\nVoce errou! o seu chute foi menor do que o numero secreto")
            if(rodada == numero_premiado):
                print("Voce perdeu, o numero era: {}".format(numero_premiado))
                print("Voce fez: {}".format(pontos))

print("Fim de jogo")


