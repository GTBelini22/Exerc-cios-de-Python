def usuario_escolhe_jogada(nu,mu):
    i = False
    while i== False:
        xu = int(input("Quantas peças você vai tirar?"))
        if xu<=mu and xu<=nu and xu>0:
            i =True
            return xu
        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")


def computador_escolhe_jogada(nc,mc):
    xc = 1
    controle_c = False

    if nc<=mc:
        xc = nc
        controle_c = True

    count = 0
    aux =nc

    while controle_c == False:
        count +=1
        aux -=1
        if aux%(mc+1)== 0:
            xc = count
            controle_c =True
        elif count == mc:
            controle_c = True

    if controle_c == False:
        xc = mc

    return xc



def partida():
    w = False
    while w == False:
        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças por jogada?"))
        if n>0 and m>0:
            w = True
        else:
            print("números Invalidos! tente novamente")
    controle = False
    r = 1
    v = m+1
    if n%v==0:
        print("\nVoce começa!\n")
        while controle == False:
            escolha_usuario = usuario_escolhe_jogada(n,m)
            if escolha_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou ", escolha_usuario, "peças.")

            if escolha_usuario == n:
                print("Fim do jogo! Você ganhou!")
                n -= escolha_usuario
                controle == True
                r =0
                break
            else:
                n -= escolha_usuario
                print("Agora restam ", n, "peças no tabuleiro.\n")


            if n!=0:
                escolha_computador = computador_escolhe_jogada(n,m)
                if escolha_computador == 1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou ", escolha_computador, "peças.")

                if escolha_computador == n:
                    print("Fim do jogo! O computador ganhou!")
                    n -= escolha_computador
                    r=1
                    controle == True
                    break
                else:
                    n -= escolha_computador
                    print("Agora restam", n, "peças no tabuleiro.\n")

    else:
        print("\nComputador começa!\n")
        while controle == False:
            escolha_computador =  computador_escolhe_jogada(n, m)
            if escolha_computador == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou ",escolha_computador ,"peças.")

            if escolha_computador == n:
                print("\nFim do jogo! O computador ganhou!")
                n -= escolha_computador
                r=1
                controle = True
            else:
                n -= escolha_computador
                print("Agora restam",n ,"peças no tabuleiro.\n")


            if n!=0:
                escolha_usuario = usuario_escolhe_jogada(n, m)

                if escolha_usuario == 1:
                    print("\nVocê tirou uma peça.")
                else:
                    print("\nVocê tirou ", escolha_usuario, "peças.")

                if escolha_usuario == n:
                    print("\nFim do jogo! Você ganhou!")
                    r=0
                    n -= escolha_usuario
                    controle = True
                else:
                    n -= escolha_usuario
                    print("Agora restam ",n,"peças no tabuleiro.\n")


    return r
escolha =0
confirm = False
countc = 0
countu = 0

while escolha ==0 or confirm == False:
    escolha = int(input("Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para joga um campeonato!"))
    if escolha ==1:
        print("\nVoce escolheu uma partida isolada!\n")
        confirm =True
    elif escolha ==2:
        print("\nVoce escolheu um campeonato!\n")
        confirm =True
    else:
        print("\nValor inserido incorreto! Tente novamente\n")

if escolha ==1:
    print("**** Rodada 1 ****\n")
    partida()
else:
    print("**** Rodada 1 ****\n")
    result = partida()
    if result==1:
        countc+=1
    else:
        countu+=1
    print("**** Rodada 2 ****\n")
    result = partida()
    if result == 1:
        countc += 1
    else:
        countu += 1
    print("**** Rodada 3 ****\n")
    result = partida()
    if result == 1:
        countc += 1
    else:
        countu += 1
    print("**** Final do campeonato! ****")

    print("Placar: Você ",countu ," X ",countc  ," Computador")
