# >>> Importa os modulos necessarios <<<
from random import randint
from time import sleep
import os
# <<<------------------------------>>>



# >>> Define a Classe Celula <<<
class Celula:
    def __init__(self, status, tabu):
        self.__status = status
        self.__master = tabu
    def __str__(self):
        if self.__status == 0:
            return "."
        elif self.__status == 1:
            return "o"
    def matar(self):
        if self.__status == 1:
            self.__status = 0
            self.__master._cel_vivas -= 1
    def reviver(self):
        if self.__status == 0:
            self.__status = 1
            self.__master._cel_vivas += 1
    @property
    def status(self):
        return self.__status
# <<<------------------------------>>>



# >>> Define a Classe Tabuleiro <<<
class Tabuleiro:
    def __init__(self, w, h):
        tabuleiro = []
        for i in range(h):
            lista = []
            for i in range(w):
                c = Celula(0, self)
                lista.append(c)
            tabuleiro.append(lista)
        self.jogo = tabuleiro
        self.__morre = []
        self.__revive = []
        self.__w = w
        self.__h = h
        self._cel_vivas = 0

    def __str__(self):
            return "Tabuleiro do jogo da vida de Conway"

    def mostrar_tabuleiro(self):
        for i in self.jogo:
            for j in i:
                print(j, end=" ")
            print()
        print()

    def contar_tabuleiro(self, y, x):
        if y > 0 and y < self.__h-1:
            if x > 0 and x < self.__w-1:
                return (self.jogo[y-1][x-1].status + self.jogo[y-1][x].status + self.jogo[y-1][x+1].status + self.jogo[y][x-1].status + self.jogo[y][x+1].status + self.jogo[y+1][x-1].status + self.jogo[y+1][x].status + self.jogo[y+1][x+1].status)
            elif x == self.__w-1:
                return (self.jogo[y-1][x-1].status + self.jogo[y-1][x].status + self.jogo[y][x-1].status + self.jogo[y+1][x-1].status + self.jogo[y+1][x].status)
            elif x == 0:
                return (self.jogo[y-1][x].status + self.jogo[y-1][x+1].status + self.jogo[y][x+1].status + self.jogo[y+1][x].status + self.jogo[y+1][x+1].status)
        elif y == self.__h-1:
            if x > 0 and x < self.__w-1:
                return (self.jogo[y-1][x-1].status + self.jogo[y-1][x].status + self.jogo[y-1][x+1].status + self.jogo[y][x-1].status + self.jogo[y][x+1].status)
            elif x == self.__w-1:
                return (self.jogo[y-1][x-1].status + self.jogo[y-1][x].status + self.jogo[y][x-1].status)
            elif x == 0:
                return (self.jogo[y-1][x].status + self.jogo[y-1][x+1].status + self.jogo[y][x+1].status)
        elif y == 0:
            if x > 0 and x < self.__w-1:
                return (self.jogo[y][x-1].status + self.jogo[y][x+1].status + self.jogo[y+1][x-1].status + self.jogo[y+1][x].status + self.jogo[y+1][x+1].status)
            elif x == self.__w-1:
                return (self.jogo[y][x-1].status + self.jogo[y+1][x-1].status + self.jogo[y+1][x].status)
            elif x == 0:
                return (self.jogo[y][x+1].status + self.jogo[y+1][x].status + self.jogo[y+1][x+1].status)

    def avaliar(self):
        for i in range(len(self.jogo)):
            for j in range(len(self.jogo[i])):
                if self.jogo[i][j].status == 1:
                    if (self.contar_tabuleiro(i, j) < 2) or (self.contar_tabuleiro(i, j) > 3):
                        self.__morre.append((i, j))         
                elif self.jogo[i][j].status == 0:
                    if self.contar_tabuleiro(i, j) == 3:
                        self.__revive.append((i, j))

    def randomizar(self, cel_inicio):
        self.__cel_vivas = cel_inicio
        for celula in range(cel_inicio):
            while True:
                x, y = randint(0, width-1), randint(0, height-1)
                if self.jogo[y][x].status == 0:
                    self.jogo[y][x].reviver()
                    break

    def limpar_morre(self):
        self.__morre = []

    def limpar_revive(self):
        self.__revive = []

    @property
    def morre(self):
        return self.__morre
        
    @property
    def revive(self):
        return self.__revive
    @property
    def width(self):
        return self.__w

    @property
    def height(self):
        return self.__h
# <<<------------------------------>>>


while True:
    print("\tO Jogo da Vida de Conway\n")
    
    # >>> Pede as dimensoes pro usuario <<<
    while True:
        try:
            width = int(input("Digite a largura do tabuleiro: "))
            break
        except:
            print("A entrada deve ser um número inteiro.")

    while True:        
        try:
            height = int(input("Digite a altura do tabuleiro: "))
            break
        except:
            print("A entrada deve ser um número inteiro.")

    print()
    # <<<------------------------------>>>



    # >>> Cria e arruma o tabuleiro <<<
    vida = Tabuleiro(width, height)
    # <<<------------------------------>>>



    # >>> Define a quantidade inicial de celulas vivas e as coloca no tabuleiro <<<
    while True:
        try:
            sel = int(input("Digite 1 para inserir/remover uma célula no tabuleiro.\nDigite 2 para geração aleatória.\nDigite outro número para sair.\nSeleção: "))
            os.system('cls')
            break
        except:
            print("A seleção deve ser um número.")
            os.system('cls')

    if sel == 1:
        while True:
            print("\tO Jogo da Vida de Conway")
            print("Células Vivas: ", vida._cel_vivas)
            vida.mostrar_tabuleiro()
            try:
                tirar_botar = int(input("Digite 1 para adicionar uma célula ou 2 para remover: "))
            except:
                print("Você deve um número.")
            try:
                cord = input("Digite a coordenada no modelo (x,y) para adicioná-la ao tabuleiro, ou\nDigite 'vai' para iniciar o jogo, ou\nDigite 'sair' para fechar o programa\n>>> ")
                if cord == 'vai':
                    break
                elif cord == 'sair':
                    raise SystemExit
                cord = cord.replace('(', '')
                cord = cord.replace(')', '')
                cord = cord.strip(',')
                x, y = cord.split(',')
                x, y = int(x), int(y)
                if x < 0 or x >= width or y < 0 or y >= height:
                    raise ValueError('ops')
                else:
                    if tirar_botar == 1:
                        vida.jogo[y][x].reviver()
                    elif tirar_botar == 2:
                        vida.jogo[y][x].matar()
                    else:
                        raise ValueError('ops')
            except SystemExit:
                raise SystemExit
            except:
                print("Opa, alguma coisa deu errado, aguarde...")
                sleep(1.5)
            os.system('cls')
                
    elif sel == 2:
        print("\tO Jogo da Vida de Conway\n")
        inicial = int(input("Digite a quantidade inicial de células (max = %d): "%(width*height)))
        if inicial <= width*height and inicial > 0:
            celulas_inicio = inicial
            vida.randomizar(celulas_inicio)
        else:
            celulas_inicio = randint(1, (width*height))
            vida.randomizar(celulas_inicio)
    else:
        raise SystemExit
    # <<<------------------------------>>>



    # >>> ---------------------------- <<<
    geracoes = 0
    os.system('cls')
    # <<<------------------------------>>>



    # >>> }{()}{ MAIN LOOP }{()}{ <<<
    while True:
        print("\tO Jogo da Vida de Conway")
        print("Células Vivas: ", vida._cel_vivas)

        vida.mostrar_tabuleiro()
        
        vida.limpar_morre()
        vida.limpar_revive()
        vida.avaliar()

        for i in vida.morre:
            y, x = i 
            vida.jogo[y][x].matar()

        for i in vida.revive:
            y, x = i 
            vida.jogo[y][x].reviver()

        #sleep(0.5)

        os.system('cls')
        
        if vida.morre == vida.revive:
            if vida._cel_vivas > 0:
                print("\tO Jogo da Vida de Conway")
                print("Células Vivas: ", vida._cel_vivas)
                vida.mostrar_tabuleiro()
                if geracoes > 1:
                    print("As células se modificaram por %d gerações, mas viverão para sempre!"%geracoes)
                else:
                    print("As células se modificaram por %d geração, mas viverão para sempre!"%geracoes)
            else:
                print("\tO Jogo da Vida de Conway\n")
                print("As celulas sobreviveram por %d gerações."%geracoes)
            continuar = int(input("Digite '1' para jogar de novo, ou outro número para fechar.\n>>> "))
            if continuar == 1:
                os.system('cls')
                break
            else:
                raise SystemExit
        
        geracoes += 1
    # <<<==============================>>>
