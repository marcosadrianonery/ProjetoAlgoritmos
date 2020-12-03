
# Solucionador de sudoku

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0080366  |  Moacir Mascarenha |
| 15/0062567  |  Marcos Adriano Nery |

## Sobre 
O algoritmo é capaz de solucionar sudoku que o usuário der de entrada, utilizando conhecimento adquirido na disciplina.

Sudoku, por vezes escrito Su Doku é um jogo baseado na colocação lógica de números. O objetivo do jogo é a colocação de números de 1 a 9 em cada uma das células vazias numa grade de 9x9, constituída por 3x3 subgrades chamadas regiões. O quebra-cabeça contém algumas pistas iniciais, que são números inseridos em algumas células, de maneira a permitir uma indução ou dedução dos números em células que estejam vazias. Cada coluna, linha e região só pode ter um número de cada um dos 1 a 9. Resolver o problema requer apenas raciocínio lógico e algum tempo. Os problemas são normalmente classificados em relação à sua realização. O aspecto do sudoku lembra outros quebra-cabeças de jornal. Ao contrário do que se possa pensar, o Sudoku pode-se cometer. Portanto a frase "cometer o Sudoku" está correta. Foi criado por Howard Garns, um projetista e arquiteto de 74 anos aposentado [1].



## Screenshots

### Resultados obtidos via terminal

![Imagem1](./jogoSudoku/img/imagem1.png)

### Interface de entrada para o usuário

![Imagem2](./jogoSudoku/img/imagem2.png)

### Resultados na interface

![Imagem3](./jogoSudoku/img/imagem3.png)


## Sobre o Algoritimo

#### Recursive backtracker using Depth-First Search

- 1. Make the initial cell the current cell and mark it as visited <br>
- 2. While there are unvisited cells <br>
    - 1. If the current cell has any neighbours which have not been visited <br>
        - 1. Choose randomly one of the unvisited neighbours <br>
        - 2. Push the current cell to the stack <br>
        - 3. Remove the wall between the current cell and the chosen cell <br>
        - 4. Make the chosen cell the current cell and mark it as visited <br>
    - 2. Else if stack is not empty <br>
        - 1. Pop a cell from the stack <br>
        - 2. Make it the current cell <br>

## Instalação 
**Linguagem**: Python<br>
**Framework**: <br>
<!-- Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários. -->
###  Clonar o Repositório

> git clone https://github.com/projeto-de-algoritmos/Grafos1_Trab1.git

### Instalar dependencias

> pip3 install -r requirements.txt --user

## Uso
### Link para video:

> https://www.dropbox.com/s/17qgoi084b00xjb/fascinatingindicesjokewearily%20on%202020-09-08%2002-26.mp4?dl=0

### Rodar a Aplicação

> python3 main.py

> Escolha a opção de solução 1 Utilizando Busca em largura e 2 para Busca em profundidade

> Clicar em "resolver !"(em vermelho)

## Referêcias 
> [1] https://pt.wikipedia.org/wiki/Sudoku
<!-- Quaisquer outras informações sobre seu projeto podem ser descritas abaixo. -->
> [2] https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/




