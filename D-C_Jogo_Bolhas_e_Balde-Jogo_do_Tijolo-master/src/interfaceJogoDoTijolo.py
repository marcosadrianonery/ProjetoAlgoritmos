# from bookings import possiveisHorarios, quartosNecessarios
from tkinter import *
import re
import random
import numpy as np
import jogoDoTijolo

janela = Tk()

janela.title("Jogo do tijolo")

windowWidth = janela.winfo_reqwidth()
windowHeight = janela.winfo_reqheight()
positionRight = int(janela.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(janela.winfo_screenheight()/2 - windowHeight/2)
janela.geometry("450x440+{}+{}".format(positionRight, positionDown))

lbl = Label(janela, text="Bem vindo ao Jogo do Tijolo",fg="black",font=('Arial',15))
lbl.place(x=100,y=15)
lbl1 = Label(janela, text="Entre com a idade dos jogadores e decubra o capitão!",fg="black",font=('Arial',13))
lbl1.place(x=25,y=47)
lbl2 = Label(janela, text="ex: 12 18 15 11", font=('Arial',11))
lbl2.place(x=10,y=80)



inputEntrada = Entry(janela,width=52)
inputEntrada.place(x=10,y=122)
resultadoLabel = Label(janela, text="Resultado",fg="black",font=('Arial',14))
resultadoLabel.place(x=10,y=150)


caixaTexto = Text(janela, height=15,width=61, font=('Arial',10))
caixaTexto.place(x=10, y=200)


def regras():

    textRegras =    """Regras(adaptadas): 
    Jogo de tijolo é um jogo de equipe. Cada equipe é constituída por um 
    número ímpar de jogadores. O número de jogadores deve ser maior do que 1.
    
    A falta de comunicação entre dois jogadores depende da sua diferença de 
    idade, ou seja, é maior se a diferença de idade for maior. Assim, eles 
    selecionam o capitão de uma equipe de maneira que a quantidade de 
    jogadores desta equipe que são mais jovens e mais velhos do que ele é igual.
    
    Mais inf:https://www.urionlinejudge.com.br/judge/pt/problems/view/1436"""

    caixaTexto = Text(janela, height=15,width=61, font=('Arial',10))
    caixaTexto.insert(END,textRegras)
    caixaTexto.place(x=10, y=200)

def clicked():
    valorEntrada = inputEntrada.get()
    if(valorEntrada):
        entrada = []
        entrada = valorEntrada.split(' ')
        valores = []
        for val in entrada:
            valores.append(int(val))
        
        result = jogoDoTijolo.jogoDoTijolo(valores)
        
        
        caixaTexto = Text(janela, height=15,width=61, font=('Arial',10))
        caixaTexto.insert(END,result)
        caixaTexto.place(x=10, y=200)
    else:
        result = "Entrada vazia!"
        caixaTexto = Text(janela, height=15,width=61, font=('Arial',10))
        caixaTexto.insert(END,result)
        caixaTexto.place(x=10, y=200)



btn = Button(janela, text="Buscar", command=clicked)
btn.place(x=278,y=150)

btn = Button(janela, text="Regras", command=regras)
btn.place(x=342,y=150)

regras()

janela.mainloop()