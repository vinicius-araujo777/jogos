from colorama import *
ORANGE = "\033[38;5;208m"
import random
import time




def menu():
    print (f'{Fore.LIGHTWHITE_EX} 1 - Jogo dos dados ')
    print (f'{Fore.LIGHTWHITE_EX} 2 - Blackjack ')
    print (f'{Fore.LIGHTWHITE_EX} 0 - sair')


def dados():
    dado_jogado = int(input(f'{Fore.LIGHTBLACK_EX}Tente a sorte com um número de 1 a 6: '))

    if dado_jogado < 1 or dado_jogado > 6:
        print (f'{Fore.RED} ERRO! Digite um número entre 1 e 6. ')
        return False

    resultado = random.randint(1, 6)
    print(f'{Fore.LIGHTWHITE_EX}o dado foi girado...')
    time.sleep(1.5)
    print(f'{Fore.LIGHTWHITE_EX}O resultado foi: {resultado}')

    if resultado == dado_jogado:
        time.sleep(0.5)
        print (f'{Fore.GREEN}Parabéns! Você acertou e ganhou {aposta*mult}!')
        return True
        
    else:
        time.sleep(0.5)
        print (f'{Fore.RED}Que azar... você errou e perdeu {aposta}!')
        return False
       


def jogo_21():
    total_usuario = 0
    naipe_card = ['copa','paus','espada','ouro']

    def deeler():
        total = 0
        print(f'{Fore.CYAN}VEZ DO DEALER')
        while total < total_usuario:
            carta = random.randint(1, 13)
            naipe = random.choice(naipe_card)
            total += carta

            print(f'{Fore.CYAN}Dealer comprou {carta} de {naipe} / Total: {total}')
            time.sleep(0.5)
        return total
    

    while True:
        print(f'{Fore.BLUE}SUA VEZ')
        carta = random.randint(1, 13)
        if carta >= 2 and carta <= 10:
            print (f'{Fore.BLUE}Você recebeu um {carta} de {random.choice(naipe_card)} ')
            valor = carta

        elif carta == 11:
            print (f'{Fore.BLUE}Você recebeu um valete de {random.choice(naipe_card)} que equivale a {carta}.')
            valor = 11

        elif carta == 12:
            print (f'{Fore.BLUE}Você recebeu uma dama de {random.choice(naipe_card)} que equivale a {carta}.')
            valor = 12

        elif carta == 13:
            print (f'{Fore.BLUE}Você recebeu um rei de {random.choice(naipe_card)} que equivale a {carta}.')
            valor = 13

        elif carta == 1:
            print (f'{Fore.BLUE}Você recebeu um Ás de {random.choice(naipe_card)} que equivale a {carta}')
            valor = 1
        

        total_usuario += valor
        time.sleep(0.2)
        print(f'seu total é de: {total_usuario}')
        if total_usuario > 21:
            time.sleep(0.2)
            print(f'{Fore.RED} Você perdeu, pois tem mais que 21, e perdeu {aposta} ficha(s)!')
            return False
        
  
        pedir = input(f'{Fore.LIGHTWHITE_EX}Deseja pedir uma carta? (s/n)').lower()
        if pedir == 's':
            continue
        else:
            total_deeler = deeler()
            time.sleep(0.5)
            print(f'{Fore.BLUE}Seu total: {total_usuario}')
            time.sleep(0.5)
            print(f'{Fore.CYAN}Total do dealer: {total_deeler}')
            if total_deeler > 21:
                print(f'{Fore.GREEN}Dealer ultrapassou 21! Você ganhou {aposta*mult} ficha(s)!')
                return True
            elif total_deeler >= total_usuario:
                print(f'{Fore.RED}Dealer venceu! Você perdeu {aposta} ficha(s)!')
                return False
            else:
                print(f'{Fore.GREEN}Você venceu ao deeler e ganhou {aposta*mult} ficha(s)!')
                return True
    


    


saldo = 250
while True:
    menu()
    print(f'{Fore.YELLOW}seu saldo atual é: {saldo} ficha(s)')
    op = input(f'{Fore.LIGHTWHITE_EX}Oque você deseja? ')
    



    if op == '0':
        print(f'{ORANGE}Volte sempre!')
        time.sleep(0.3)
        print(f'{ORANGE}SAINDO ...')
        time.sleep(1.5)
        break

    elif op == '1':
        print('Ótima escolha! faça suas apostas e jogue os dados!')
        time.sleep(0.5)
        aposta = int(input('qual valor de aposta? '))
        if aposta > saldo:
            print(f'{Fore.RED} seu saldo é de {saldo} ficha(s), você não pode apostar {aposta} ficha(s)')
            continue
        mult = int(input('digite seu multiplicador, (De 1x à 10x): '))
        if mult > 10 or mult < 1:
            print(f'o multiplicador {mult} é invalido!')
            continue

        ganhou = dados()
        if ganhou:
            saldo += aposta*mult
        else:
            saldo -= aposta


    elif op == '2':
        print('Ótima escolha! faça suas apostas e tente chegar o mais proximo de 21!')
        time.sleep(0.5)
        aposta = int(input('qual valor de aposta? '))
        if aposta > saldo:
            print(f'{Fore.RED} seu saldo é de {saldo} ficha(s), você não pode apostar {aposta} ficha(s)')
            continue
        mult = int(input('digite seu multiplicador, (De 1x à 5x): '))
        if mult > 5 or mult < 1:
            print(f'o multiplicador {mult} é invalido!')
            continue

        ganhou = jogo_21()
        if ganhou:
            saldo += aposta*mult
        else:
            saldo -= aposta

            
    else:
        print(f'{Fore.RED} opção invalida!')


    if saldo <= 0:
        print(f'{Fore.RED}Você não tem mais fichas, você perdeu!')
        reinicio = input(f'{Fore.LIGHTWHITE_EX}Deseja jogar novamente? (s/n)').lower()
        if reinicio == 's':
            saldo = 250
        else:
            break