import sys
from copy import deepcopy


# Python3 code for the above approach. [(entrada-saida)]
def possiveisHorarios(entrada, numero_quartos): 
    ans = []
    # numero_quartos = k
    quartos = {}
    log = []
    for i in range(1, numero_quartos + 1):
        quartos[i] = ['Vazio', (0, 0)]

    for i in range(0, len(entrada)): 
        ans.append((entrada[i][0], entrada[i][1]))
    
    ans.sort()
    curr_active, max_active = 0, 0
    ans_iter = deepcopy(ans)
    for m in ans_iter:
        for quarto in quartos:
            if quartos[quarto][0] == 'Vazio':
                quartos[quarto] = ['Ocupado', m]
                curr_active += 1
                ans.remove(m)
                max_active = max(max_active, curr_active) 
                log.append(str(quartos))
                break
            elif quartos[quarto][1][1] < m[0]:
                quartos[quarto] = ['Ocupado', m]
                ans.remove(m)

                curr_active -= 1
                log.append(str(quartos))
                break                
    print("Para " + str(numero_quartos) + " o log de ocupação é: " )
    for j in log:
        print(j)
    if not ans:
        return numero_quartos >= max_active, ans, log 
        print("------------------------------------------------------------------------------------------")
    else:
        print("Horarios não encaixados: ", ans)
        print("------------------------------------------------------------------------------------------")
        return numero_quartos < max_active, ans, log

# Driver Code 
# if __name__ == "__main__": 

def quartosNecessarios(entrada): 
    # entrada = [1, 3, 5, 6] 
    # saida = [2, 6, 8, 8] 
    # entrada = [1, 3, 0, 5, 6, 5, 7, 8, 11, 2, 13]
    # saida = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    report = []
    for n in range(1, len(entrada)+1):
        bol, quartos, hist = possiveisHorarios(entrada, n)
        if bol:
            # print("O numero de quartos ideal é:", n)
            report.append("O numero de quartos ideal é: " + str(n))
            break
        report.append("Para " + str(n) + " quartos é necessario alterar os horarios:  " + str(quartos))
    print("------------------------------------------------------------------------------------------")
    for j in report:
        print(j)
        print("------------------------------------------------------------------------------------------")
    voltar = report
    return voltar


# def tratarDados(valorEntrada):

#     entrada = []
#     saida = []

#     for horario in valorEntrada:
#         entradaTemp = ""
#         saidaTemp = ""
#         temp = 0

#         horario.strip(" ")

#         for i in horario:
#             if i == ' ':
#                 # print("spaced")
#                 None
#             elif i == '-':
#                 temp = 1
#             elif temp == 0:
#                 # entradaTemp.append(i)
#                 entradaTemp = entradaTemp + i

#             elif temp == 1:
#                 # saidaTemp.append(i)
#                 saidaTemp = saidaTemp + i

#         entrada.append(int(entradaTemp))
#         saida.append(int(saidaTemp))

#     # numero_quartos = 2
#     test = quartosNecessarios(entrada, saida)

#     # print("Report", test)
#     # print("Entrada: ", entrada)
#     # print("Saida: ", saida)
#     # print(valorEntrada)

#     texto = ""

#     for partText in test:
#         texto = texto + str(partText) + '\n'

#     return texto






