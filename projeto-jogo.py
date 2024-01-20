"""
Trabalho em grupo
Turma: 20
Desafio: Jogo de Adivinha
"""

print('Jogo da Advinhação')

def jogo_adivinhacao():
  numero_secreto = random.randint(1, 101)
  tentativas = 0
  palpite = int(input('Digite seu palpite de 1 até 100: '))
