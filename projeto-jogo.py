import random
from time import sleep
def jogo_adivinhacao():
    try:

        jogador = int(input('||  Digite um número de 1 a 100: '))
        computador = random.randint(0, 100)
        
        while True:
            
            if jogador < computador:
                print(f'INCORRETO! Tente novamente.')
                jogador = int(input('||  Digite um número MAIOR: '))
            elif jogador > computador:
                print(f'INCORRETO! Tente novamente.')
                jogador = int(input('||  Digite um número MENOR: '))
                continue
            elif jogador == computador:
                print(f'VOCÊ ACERTOU!')
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
