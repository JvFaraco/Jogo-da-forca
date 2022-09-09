import random
import os


def inicio():
    while True:
        print('------------------------------------------------')
        print('                  JOGO DA FORCA                 ')
        print('------------------------------------------------')
        print('                    feito por joão victor faraco')
        print('[1] JOGAR')
        print('[2] SAIR DO JOGO')
        res1 = int(input(': '))
        if res1 == 1:
            return
        if res1 == 2:
            exit()
        if (res1 != 1) or (res1 != 2):
            os.system('cls')


def palavrasecreta():
    times = ['flamengo', 'gremio', 'palmeiras', 'vasco',
             'cruzeiro', 'avai', 'figueirense', 'santos', 'corinthians']
    numero = random.randrange(0, len(times))
    timesecreto = times[numero].upper()
    return timesecreto


def iniciopalavra(palavra):

    return ['_' for letra in palavra]


def menu(secreto, letra, jogo):
    while j == 0:
        print(letra)
        print(' ')
        print('[1] TENTAR CHUTE')
        print('[2] ADIVINHAR A PALAVRA')
        res2 = int(input(': '))
        if res2 == 1:
            j = 1
        if res2 == 2:
            j = 1
            print(letra)
            print(' ')
            print('QUAL É O TIME?')
            time = str(input(': '))
            if time.upper() == secreto:
                ganhou(secreto, jogo)
            else:
                perdeu(secreto, jogo)


def chutes():
    chute = str(input('Qual o seu chute? '))
    chute = chute.strip().upper()
    return chute


def chutecorreto(chute, letracerta, timesecreto):
    i = 0
    for letra in timesecreto:
        if letra == chute:
            if chute in letracerta[i]:
                print('Você já digitou essa letra')
            letracerta[i] = letra
            print(letracerta)
        i += 1


def ganhou(secreto, jogo):
    print('PARABÉNS VOCÊ GANHOU!')
    print(f'A PALAVRA SECRETA ERA {secreto}')
    print('DESEJA JOGAR NOVAMENTE? (S/N) ')
    res1 = str(input(': '))
    if res1.upper() == 'S':
        os.system('cls')
        jogar()
    else:
        os.system('cls')
        print('------------------------------------------------')
        print('                    FIM DE JOGO                 ')
        print('------------------------------------------------')
        quit()


def perdeu(secreto, jogo):
    print('VOCÊ NÃO CONSEGUIU CONCLUIR O JOGO!')
    print(f'A PALAVRA SECRETA ERA {secreto}')
    print('DESEJA JOGAR NOVAMENTE? (S/N) ')
    res1 = str(input(': '))
    if res1.upper() == 'S':
        os.system('cls')
        jogar()
    else:
        os.system('cls')
        print('------------------------------------------------')
        print('                    FIM DE JOGO                 ')
        print('------------------------------------------------')
        quit()


def jogar():
    inicio()
    timesecreto = palavrasecreta()
    letracerta = iniciopalavra(timesecreto)
    fim = False
    ganhar = False
    erro = 0
    while (not fim and not ganhar):
        j = 0
        print(letracerta)
        while j == 0:
            letrasfaltando = str(letracerta.count('_'))
            if letrasfaltando == '0':
                ganhar == True
                ganhou(timesecreto, jogar)
            print(' ')
            print('[1] TENTAR CHUTE')
            print('[2] ADIVINHAR A PALAVRA')
            res2 = int(input(': '))
            if res2 == 1:
                chute = chutes()
                if (chute in timesecreto):
                    chutecorreto(chute, letracerta, timesecreto)
                else:
                    erro += 1
                    print(letracerta)
                    print(f'Você errou, ainda tem {7 - erro} chances ')
                    print(f'Ainda faltam acertar {letrasfaltando} letras')
                if erro == 7:
                    fim = erro
                    perdeu(timesecreto, jogar)
            if res2 == 2:
                j = 1
                print(letracerta)
                print(' ')
                print('QUAL É O TIME?')
                time = str(input(': '))
                if time.upper() == timesecreto:
                    ganhou(timesecreto, jogar)
                else:
                    perdeu(timesecreto, jogar)


jogar()
