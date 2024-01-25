"""
Trabalho em grupo.
Turma: 20
Grupo: C
Desafio: Desenvolver um jogo de adivinha
"""

import random
from time import sleep


# função do jogo de adivinhação de um número entre 1 e 100
def jogo_adivinhacao():
    while True:
        try:
            # Número de tentativas
            tentativas = 1

            # Solicitação ao usuário de um número de 1 até 100
            jogador = int(input('||          Digite um número de 1 a 100: '))

            computador = random.randint(1, 100)

            while tentativas < 15:
                if jogador < 1 or jogador > 100:
                    print('||{: ^50}||'.format('NUMERO INVALIDO!'))
                    # Solicitação ao usuário de um número de 1 até 100
                    jogador = int(input('||          Digite um número de 1 a 100: '))

                elif jogador == computador:
                    if tentativas <= 5:
                        print(f'||   Você acertou em {tentativas} tentativas! VOCÊ É SÊNIOR!   ||')
                        
                    elif tentativas <= 10:
                        print(f'||    Você acertou em {tentativas} tentativas! VOCÊ É PLENO!   ||')
                        
                    else:
                        print(f'||   Você acertou em {tentativas} tentativas! VOCÊ É JÚNIOR!   ||')

                    print('||{: ^50}||'.format('FIM DE JOGO!'))
                    print('=' * 54)
                    break

                elif jogador < computador:
                    print('||{: ^50}||'.format('INCORRETO! Tente Novamente.'))
                    jogador = int(input('||          Digite um número MAIOR: '))
                elif jogador > computador:
                    print('||{: ^50}||'.format('INCORRETO! Tente Novamente.'))
                    jogador = int(input('||          Digite um número MENOR: '))

                tentativas += 1

                if tentativas == 15:
                    print('||{: ^50}||'.format('Você atingiu o número máximo de tentativas.'))
                    print('||{: ^50}||'.format('O computador é o vencedor!'))
                    print('||{: ^50}||'.format('FIM DO JOGO!'))
                    print('=' * 54)

            jogar_novamente = input('||          Deseja jogar novamente? (S/N): ').upper()
            if jogar_novamente != 'S':
                print('||{: ^50}||'.format('FIM DO JOGO!'))
                print('=' * 54)
                break

        except:
            print('||{: ^50}||'.format('VALOR INVÁLIDO!'))
            print('=' * 54)


print('=' * 54)
print('||{: ^50}||'.format('JOGO DA ADVINHAÇÃO'))
print('=' * 54)
sleep(1)

print('||{: ^50}||'.format('Vamos jogar? Se  você  adivinhar'))
print('||{: ^50}||'.format('o número que pensei, você ganha.'))
print('||{: ^50}||'.format('Você tem 15 tentativas!'))
print('=' * 54)

print('||{: ^50}||'.format('3...'))
sleep(0.5)
print('||{: ^50}||'.format('2...'))
sleep(0.5)
print('||{: ^50}||'.format('1...'))
sleep(0.5)
print('||{: ^50}||'.format('Pensei'))
sleep(0.5)
print('=' * 54)

jogo_adivinhacao()
