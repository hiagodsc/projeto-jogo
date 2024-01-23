"""
Trabalho em grupo
Turma: 20
Desafio: Jogo de Adivinhação
"""
from random import randint

print('\n\nJogo da Adivinhação')
print('Adivinhe o número secreto!')


def jogo_adivinhacao():

  a = True
  numero_secreto = randint(1, 101)
  tentativas = 0

  while a == True:  

    palpite = int(input("Digite seu palpite de 1 até 100: "))

    if palpite == numero_secreto:
      print("\nParabéns")
      print("Você acertou!")
      print("O número secreto é: ", numero_secreto)
      a = False

    elif palpite > numero_secreto: # Orienta se o número secreto é maior ou menor que o palpite
      print("\nVocê errou!")
      print("Tente um número menor\n")

    else:
      print("\nVocê errou!")
      print("Digite um número maior\n")
  


jogo_adivinhacao()
