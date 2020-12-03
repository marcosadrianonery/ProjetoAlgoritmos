

def main():

    print("Bem vindo D-C_Jogo_Bolhas_e_Balde-Jogo_do_Tijolo")
    print("Escolha o jogo")
    print("1 para JogoBolhas e Balde")
    print("2 para Jogo do Tijolo")
    print("3 para Sair")
    opcao = int(input('Digite aqui: '))

    if(opcao == 1):
        from interface import janela

    elif(opcao == 2):
        from interfaceJogoDoTijolo import janela
    elif(opcao == 3):
        print("Obrigado e até mais!")
    else:
        print()
        print("Opção inválida!")
        print()

        main()


main()