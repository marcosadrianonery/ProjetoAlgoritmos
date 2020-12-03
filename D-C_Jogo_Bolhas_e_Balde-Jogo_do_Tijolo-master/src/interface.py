# from bookings import possiveisHorarios, quartosNecessarios
from tkinter import *
import re
import random
import numpy as np
import utils

janela = Tk()

janela.title("Bolhas e Baldes")

windowWidth = janela.winfo_reqwidth()
windowHeight = janela.winfo_reqheight()
positionRight = int(janela.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(janela.winfo_screenheight()/2 - windowHeight/2)
janela.geometry("450x440+{}+{}".format(positionRight, positionDown))

lbl = Label(janela, text="Bem vindo ao Bolhas e Baldes",fg="black",font=('Arial',15))
lbl.place(x=100,y=15)
lbl1 = Label(janela, text="Escolha a melhor sequencia e se divirta!",fg="black",font=('Arial',13))
lbl1.place(x=65,y=47)
lbl2 = Label(janela, text="Não é necessario indicar a quantidade de entradas.", font=('Arial',11))
lbl2.place(x=10,y=80)
lbl3 = Label(janela, text="Ex: 6 5 4 3 2 1      Ex: [ 6, 5, 4, 3, 2, 1]", font=('Arial',11))
lbl3.place(x=10,y=100)


inputEntrada = Entry(janela,width=52)
inputEntrada.place(x=10,y=122)
resultadoLabel = Label(janela, text="Resultado",fg="black",font=('Arial',14))
resultadoLabel.place(x=10,y=185)

caixaTexto = Text(janela, height=9,width=61, font=('Arial',10))
caixaTextoJogador1 = Text(janela, height=1,width=61, font=('Arial',10))
caixaTextoJogador2 = Text(janela, height=1,width=61, font=('Arial',10))
caixaTextoJogador1.place(x=10, y=210)
caixaTextoJogador2.place(x=10, y=245)

caixaTexto.place(x=10, y=280)

nomeJogador1 = "Jogador numero 1"
nomeJogador2 = "Jogador numero 2"

def regras():

    textRegras =    """O jogo consiste em cada jogador fazer um movimento, e a jogada passa 
para o outro jogador. O primeiro jogador é sempre o primeiro a começar
a jogar. Um movimento de um jogador consiste na escolha de um par de 
elementos consecutivos da seqüência que estejam fora de ordem e em 
inverter a ordem dos dois elementos. Por exemplo, dada a seqüência 
1, 5, 3, 4, 2, o jogador pode inverter as posições de 5 e 3 ou de 4 e 2, 
mas não pode inverter as posições de 3 e 4, nem de 5 e 2. 
Continuando com o exemplo, se o jogador decide inverter as posições
de 5 e 3 então a nova seqüência será 1, 3, 5, 4, 2.
Mais inf: https://www.urionlinejudge.com.br/judge/pt/problems/view/1088"""

    caixaTexto = Text(janela, height=9,width=61, font=('Arial',10))
    caixaTexto.insert(END,textRegras)
    caixaTexto.place(x=10, y=280)

def clicked():
    
    global nomeJogador1
    global nomeJogador2

    erro =  '   Entrada inválida "{}", formato válido compõe \n' + '   numeros de 1 a 9 que preservem a sequencia, \n' + '   espaços são permitidos \n\n   Por favor, tente novamente.'
    alerta = 0
    valorEntrada = inputEntrada.get()

    try:
        # valorEntrada = valorEntrada.split(',')
        entrada = []
        for i in valorEntrada:

            if not re.match("[1-9, \[ \]]", i):
                erro = erro.format(i)
                alerta=1
                break

            if re.match("[1-9]",i):
                entrada.append(i)

    except:
        erro=erro
        alerta = 1
    
    texto = ""
    
    if(alerta!=0):
        texto = erro

    else:
        result = []
        result, contSol = utils.bolhaBalde(entrada)        
        # result, contSol = utils.bolhaBalde(entrada[1:])        

        if (contSol%2) == 0:
            nameList = nomeJogador2
        else:
            nameList = nomeJogador1

        test = nameList
        texto = "O nome do jogador vencedor é: "

        for partText in test:
            texto = texto + str(partText)
    
    caixaTexto = Text(janela, height=9,width=61, font=('Arial',10))
    caixaTexto.insert(END,texto)
    caixaTexto.place(x=10, y=280)

def nameJogador1():
    
    global nomeJogador1

    valorEntrada = inputEntrada.get()
    valorEntradaLimpa = valorEntrada
    nomeJogador1 = valorEntradaLimpa
    textJogador1 = "O nome do jogador 1 é: " + str(nomeJogador1)    
    text = " Você definiu o nome do Jogador 1: " + str(nomeJogador1) + ", \n caso queira alterar basta digitar o nome e clicar \n novamente no botão 'Nome jogador 1'. \n\n Por favor, digite o nome do segundo jogador e \n click no botão 'Nome jogador 1'.!"

    caixaTextoJogador1 = Text(janela, height=1,width=61, font=('Arial',10))
    caixaTextoJogador1.insert(END,textJogador1)
    caixaTextoJogador1.place(x=10, y=210)
    caixaTexto = Text(janela, height=9,width=61, font=('Arial',10))
    caixaTexto.insert(END,text)
    caixaTexto.place(x=10, y=280)

def nameJogador2():
    
    global nomeJogador2

    valorEntrada = inputEntrada.get()
    valorEntradaLimpa = valorEntrada
    nomeJogador2 = valorEntradaLimpa
    textJogador2 = "O nome do jogador 2 é: " + str(nomeJogador2)    
    text = " Você definiu o nome do Jogador 2: " + str(nomeJogador2) + ", \n caso queira alterar basta digitar o nome e clicar \n novamente no botão 'Nome jogador 2'. \n\n Por favor, digite a sequencia do jogo e \n click no botão 'Jogar'.!"

    caixaTextoJogador2 = Text(janela, height=1,width=61, font=('Arial',10))
    caixaTextoJogador2.insert(END,textJogador2)
    caixaTextoJogador2.place(x=10, y=245)
    caixaTexto = Text(janela, height=9,width=61, font=('Arial',10))
    caixaTexto.insert(END,text)
    caixaTexto.place(x=10, y=280)


btn = Button(janela, text="Nome Jogador 1", command=nameJogador1)
btn.place(x=10,y=150)

btn = Button(janela, text="Nome Jogador 2", command=nameJogador2)
btn.place(x=144,y=150)

btn = Button(janela, text="Jogar", command=clicked)
btn.place(x=278,y=150)

btn = Button(janela, text="Regras", command=regras)
btn.place(x=342,y=150)

regras()

janela.mainloop()