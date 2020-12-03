from bookings import possiveisHorarios, quartosNecessarios
from tkinter import *
import re

janela = Tk()

janela.title("Hotel HOTEL")

windowWidth = janela.winfo_reqwidth()
windowHeight = janela.winfo_reqheight()
positionRight = int(janela.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(janela.winfo_screenheight()/2 - windowHeight/2)

# janela.geometry('350x400+0+0')

janela.geometry("450x465+{}+{}".format(positionRight, positionDown))

lbl = Label(janela, text="Bem vindo ao hotel",fg="black",font=('Arial',15))
lbl.place(x=140,y=0)

lbl1 = Label(janela, text="Entre com as reservas antecipadas!",fg="black",font=('Arial',13))
lbl1.place(x=80,y=25)


lbl2 = Label(janela, text="Dias (ex:1-2,3-5):", font=('Arial',11))
lbl2.place(x=10,y=53)

inputEntrada = Entry(janela,width=52)
inputEntrada.place(x=10,y=78)

resultadoLabel = Label(janela, text="Resultado",fg="white",font=('Arial',14))
resultadoLabel.place(x=10,y=160)
resultadoLabel.configure(background='blue')


caixaTexto = Text(janela, height=14,width=53, fg="white")
# caixaTexto.insert(END,texto)
caixaTexto.place(x=10, y=190)
# caixaTexto.configure(background='black')

def clicked():
    erro="""Entrada inválida {}
formato válido ex:1-4,5-6
tente novamente"""
    alerta = 0
    valorEntrada = inputEntrada.get()

    try:
        valorEntrada = valorEntrada.split(',')
        entrada = []
        for i in valorEntrada:
            if not re.match("[0-9]+-[0-9]+",i):
                print("erro: ",i)
                erro = erro.format(i)
                alerta=1
                break
            b = i.split('-')
            entrada.append((int(b[0]),int(b[1])))
        print(entrada)
    except:
        erro=erro
        alerta = 1
    
    # print(valorEntrada)
    texto = ""
    
    if(alerta!=0):
        texto = erro
    else:
        # Chamar funções e pegar os resutados
        test = quartosNecessarios(entrada)
        texto = ""

        for partText in test:
            texto = texto + str(partText) + '\n'

    
    caixaTexto = Text(janela, height=14,width=53)
    caixaTexto.insert(END,texto)
    caixaTexto.place(x=10, y=190)


btn = Button(janela, text="Analisar", command=clicked)

btn.place(x=100,y=110)

janela.mainloop()