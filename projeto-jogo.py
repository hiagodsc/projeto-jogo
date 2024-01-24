"""
Trabalho em grupo
Turma: 20
Grupo: C
Desafio: Desenvolver um jogo de adivinha
"""

from random import randint
from time import sleep


# função do jogo de adivinhação de um número
def jogo_adivinhacao():
    try:
        # número de tentativas
        tentativas = 1

        # solicita ao usuário que digite um número de 1 até 100
        jogador = int(input('||  Digite um número de 1 a 100: '))

        computador = randint(1, 100)

        while tentativas < 5:

            if jogador == computador:
                print(f'VOCÊ ACERTOU!')
                print('FIM DE JOGO!')

            elif jogador < computador:
                print(f'INCORRETO! Tente novamente.')
                jogador = int(input('||  Digite um número MAIOR: '))

            elif jogador > computador:
                print(f'INCORRETO! Tente novamente.')
                jogador = int(input('||  Digite um número MENOR: '))

            tentativas += 1

            if tentativas == 5:
                print()
                print(f'Você atingiu o número máximo de tentativas.')
                print('FIM DE JOGO!')

    except:
        print('||{: ^36}||'.format('VALOR INVÁLIDO!'))

    print('=' * 40)


print('=' * 40)
print('||{: ^36}||'.format('JOGO DA ADVINHAÇÃO'))
print('=' * 40)
sleep(1)

print('''||  Vamos jogar? Se  você  adivinhar  ||
||  O número que pensei, você ganha.  ||
||  Você tem cinco tentativas.        ||''')

print('|| ')
print('=' * 40)

print('||{: ^36}||'.format('3...'))
sleep(0.5)
print('||{: ^36}||'.format('2...'))
sleep(0.5)
print('||{: ^36}||'.format('1...'))
sleep(0.5)
print('||{: ^36}||'.format('Pensei'))
sleep(0.5)
print('=' * 40)

jogo_adivinhacao()
