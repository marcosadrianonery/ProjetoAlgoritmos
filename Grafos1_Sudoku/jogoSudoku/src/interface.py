import pygame



class Tabuleiro:
    
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.quadrado_selecionado = False
        self.valor = None
        self.distancia = largura / 9
        self.COR_DE_FUNDO = (255,255,255)
        self.LARGURA = 540
        self.ALTURA = 600
        self.COR_LINHA = (0,0,0)
        self.COR_TEXTO_1 = (0,0,0)
        self.COR_TEXTO_2 = (255,0,0)
        self.COR_QUADRADO_SELECIONADO = (128,128,128)
        self.espessura_linha = 1
        self.entrada_sudoku = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]


    def posicaoQuadrado(self,tela, posicao_mouse):
        pos_quadrado = (int(posicao_mouse[0] // self.distancia), 
                        int(posicao_mouse[1] // self.distancia))
                       
        pygame.draw.rect(tela, 
                         self.COR_QUADRADO_SELECIONADO, 
                         (pos_quadrado[0] * self.ALTURA / 10, 
                         pos_quadrado[1] * self.LARGURA / 9,
                         self.LARGURA / 9, 
                         self.LARGURA / 9))
        
        
        return (int(posicao_mouse[0] // self.distancia),
                int(posicao_mouse[1] // self.distancia))
    

    def escreveNumero(self, tela, posicao_mouse):
        posicao_quadrado = self.posicaoQuadrado(tela,posicao_mouse)
        
        # print(posicao_quadrado)

        if self.valor != 0 and self.valor !=None:        
            fonte = pygame.font.SysFont("comicsans", 40)

            texto = fonte.render(str(self.valor), 1, (0,0,0))

            x = int(posicao_quadrado[0])
            y = int(posicao_quadrado[1])
            
            self.entrada_sudoku[y][x] = self.valor
           
            posicao_quadrado = (int(posicao_quadrado[0] * self.distancia), 
                                int(posicao_quadrado[1] * self.distancia))


            tela.blit(texto, (posicao_quadrado[0] + (self.distancia / 2) - 5, 
                              posicao_quadrado[1] + (self.distancia / 2) - 10))

        else:
            pos_quadrado = (int(posicao_mouse[0] // self.distancia), 
                            int(posicao_mouse[1] // self.distancia))
        
            self.entrada_sudoku[posicao_quadrado[0]][posicao_quadrado[1]] = 0
                            
            pygame.draw.rect(tela, 
                             (255,255,255), 
                             (pos_quadrado[0] * self.ALTURA / 10, 
                              pos_quadrado[1] * self.LARGURA / 9,
                              self.LARGURA / 9, 
                              self.LARGURA / 9))
            


    def desenhaTabuleiro(self, tela, altura, largura):
        for i in range(0,10):
            if i == 0:
                espessura_linha = 7

            if i % 3 == 0:
                espessura_linha = 3
            else:
                espessura_linha = 1
                
            # Linha horizontal
            pygame.draw.line(tela, self.COR_LINHA, (0, i*self.distancia), (largura, i*self.distancia), espessura_linha)
            
            # Linha vertical
            pygame.draw.line(tela, self.COR_LINHA, (i*self.distancia, 0), (i*self.distancia, altura-self.distancia), espessura_linha)

        self.desenhaRodape(tela)


    def desenhaRodape(self,tela ):
        # posicao_quadrado = self.posicaoQuadrado(self.distancia/2 ,self.altura-self.distancia/2)
        posicao_rodape = [(i, 9) for i in range(9)]
        resolver = 'resolver'
        resolver = [c for c in resolver]

        for i in range(9):
            pygame.draw.rect(tela, 
                            (255,0,0), 
                            (posicao_rodape[i][0] * self.ALTURA / 10, 
                            posicao_rodape[i][1] * self.LARGURA / 9,
                            self.LARGURA / 9, 
                            self.LARGURA / 9))

        self.escreveRodape(tela)

    def escreveRodape(self,tela,mensagem="Resolver!"):
        fonte = pygame.font.SysFont("comicsans", 40)
        resolver = mensagem
        resolver = [c for c in resolver]

        for i in range(9):
            texto = fonte.render(resolver[i], 1, (0,0,0))
            tela.blit(texto, (self.distancia * i + 25, 
                              self.altura - (self.distancia / 2) - 10))
    
    def escreveResultado(self, tela, resultado):
        fonte = pygame.font.SysFont("comicsans", 40)
        posicao_rodape = [(i, 9) for i in range(9)]
        
        for i in range(9):
            pygame.draw.rect(tela, 
                            (255,0,0), 
                            (posicao_rodape[i][0] * self.ALTURA / 10, 
                            posicao_rodape[i][1] * self.LARGURA / 9,
                            self.LARGURA / 9, 
                            self.LARGURA / 9))

        for i in range(9):
            for j in range(9):

                texto = fonte.render(str(resultado[i][j]), 1, (0,0,0))

            
                posicao_quadrado = ((j * self.distancia),( i* self.distancia))


                tela.blit(texto, (posicao_quadrado[0] + (self.distancia / 2) - 5, 
                                posicao_quadrado[1] + (self.distancia / 2) - 10))
                self.escreveRodape(tela,"Solucao !")


class Menu:
    
    def __init__(self):
        print("     BEM VINDO!")
        print("     INSIRA UM SUDOKU VALIDO!")
        print("DIGITE PARA BUSCA:")
        print("1 LARGURA")
        print("2 PROFUNDIDADE")
        self.busca = input(" ")
        self.COR_DE_FUNDO = (255,255,255)
        self.LARGURA = 540
        pygame.init()
        self.ALTURA = 600
        
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA))
        self.tela.fill(self.COR_DE_FUNDO)
        self.tabuleiro = Tabuleiro(self.LARGURA, self.ALTURA)
        self.playing = True
        


    def inicio(self):
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(posicao_mouse)
                    if self.tabuleiro.quadrado_selecionado is False:
                        posicao_mouse = pygame.mouse.get_pos()
                        
                        self.tabuleiro.posicaoQuadrado(self.tela,posicao_mouse)
                        self.tabuleiro.quadrado_selecionado = True
                        
                        if self.tabuleiro.posicaoQuadrado(self.tela,posicao_mouse)[1] == 9:
                            self.playing = False

                if self.playing:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.tabuleiro.valor = 1
                        if event.key == pygame.K_2:
                            self.tabuleiro.valor = 2
                        if event.key == pygame.K_3:
                            self.tabuleiro.valor = 3
                        if event.key == pygame.K_4:
                            self.tabuleiro.valor = 4
                        if event.key == pygame.K_5:
                            self.tabuleiro.valor = 5
                        if event.key == pygame.K_6:
                            self.tabuleiro.valor = 6
                        if event.key == pygame.K_7:
                            self.tabuleiro.valor = 7
                        if event.key == pygame.K_8:
                            self.tabuleiro.valor = 8
                        if event.key == pygame.K_9:
                            self.tabuleiro.valor = 9
                        if event.key == pygame.K_BACKSPACE:
                            self.tabuleiro.valor = 0
                            self.tabuleiro.escreveNumero(self.tela, posicao_mouse)
                            self.tabuleiro.valor = None
                            self.tabuleiro.quadrado_selecionado = False
                            
                        
                        if self.tabuleiro.quadrado_selecionado and self.tabuleiro.valor != None:
                            
                            # print(posicao_mouse, self.tabuleiro.valor)
                            self.tabuleiro.escreveNumero(self.tela, posicao_mouse)
                            self.tabuleiro.valor = None
                            self.tabuleiro.quadrado_selecionado = False
                            # print(self.tabuleiro.entrada_sudoku)
                        # pos_quadrado = self.tabuleiro.posicaoQuadrado(posicao_mouse)
                        
                    # if event.type ==pygame.

            self.tabuleiro.desenhaTabuleiro(self.tela,self.ALTURA,self.LARGURA)
            pygame.display.update()

        pygame.quit()
        return self.tabuleiro.entrada_sudoku
    
    def imprimeResultado(self, resultado,nome_busca):
        pygame.init()
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA))
        pygame.display.set_caption(nome_busca)
        self.tela.fill(self.COR_DE_FUNDO)
        self.tabuleiro = Tabuleiro(self.LARGURA, self.ALTURA)
        self.tabuleiro.desenhaTabuleiro(self.tela,self.ALTURA,self.LARGURA)
        self.tabuleiro.escreveResultado(self.tela, resultado)
        self.playing = True


        while self.playing:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    
                else:
                    pygame.display.update()

        pygame.quit()
