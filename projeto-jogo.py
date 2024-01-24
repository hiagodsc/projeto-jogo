"""
Trabalho em grupo.
Turma: 20
Grupo: C
Desafio: Desenvolver um jogo de adivinha
"""

import random
from time import sleep
def jogo_adivinhacao():
    try:

        jogador = int(input('||  Digite um número de 1 a 100: '))
        computador = random.randint(0, 100)

        while True:

            if jogador < computador:
                print('||{: ^36}||'.format('INCORRETO! Tente Novamente.'))
                jogador = int(input('||    Digite um número MAIOR: '))
            elif jogador > computador:
                print('||{: ^36}||'.format('INCORRETO! Tente Novamente.'))
                jogador = int(input('||    Digite um número MENOR: '))
                continue
            elif jogador == computador:
                print('||{: ^36}||'.format('VOCÊ ACERTOU!'))
                print('=' * 40)
                break

    except:
        print('||{: ^36}||'.format('VALOR INVÁLIDO!'))

        print('=' * 40)


print('=' * 40)
print('||{: ^36}||'.format('JOGO DA ADVINHAÇÃO'))
print('=' * 40)
sleep(1)

print('''||  Vamos jogar? Se  você  adivinhar  ||
||  o número que pensei, você ganha.  ||''')
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
