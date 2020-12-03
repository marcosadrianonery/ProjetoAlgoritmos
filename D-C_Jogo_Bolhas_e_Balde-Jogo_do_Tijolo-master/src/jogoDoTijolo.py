from utils import mediana

def jogoDoTijolo(entrada):
    entrada_aux = [int(x) for x in entrada]
    resultado = mediana(entrada_aux, len(entrada_aux)//2)
    saida = 'A idade do capitão é {} anos.'.format(resultado)
    return saida


