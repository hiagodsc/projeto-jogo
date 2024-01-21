import random
from time import sleep
def jogo_adivinhacao():
    while True:
        jogador = int(input('||  Digite um número de 1 a 10: '))
        computador = random.randint(0, 10)
        
        try: 
            
            
            #else:
                #print(f'INCORRETO! Tente novamente.')
            if jogador < computador:
                print(f'INCORRETO! Tente novamente.')
                jogador = int(input('||  Digite um número MAIOR: '))
            elif jogador > computador:
                print(f'INCORRETO! Tente novamente.')
                jogador = int(input('||  Digite um número MENOR: '))
                #continue
            elif jogador == computador:
                print(f'VOCÊ ACERTOU!')
                break
        except:
            print('Digite um valor válido')

print('=' * 40)
print('||         JOGO DA ADIVINHAÇÃO        ||')
print('=' * 40)

print('''||  Vamos jogar? Se  você  adivinhar  ||
||  o número que pensei, você ganha.  ||''')
print('=' * 40)
jogo_adivinhacao()
