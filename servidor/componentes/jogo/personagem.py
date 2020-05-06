'''
Created on 28 de abr de 2020

@author: leonardo

Content: Classe Personagem
'''
from componentes.jogo.objetos_dinamicos import ObjetosDinamicos
from componentes.jogo.bomba import Bomba
from componentes.jogo.thread_update import ThreadUpdate

import math

class Personagem(ObjetosDinamicos):
    #Constante de tempo.
    TIMER = 1.0

    def __init__(self, sid, posicao_x, posicao_y,
                 direcao_x = 0, direcao_y = 0,
                 raio_bomba = 3, count_bomba = 1,
                 distancia_bomba = 1, angulo_bomba = 0):

        #Chama o construtor da classe mãe
        super().__init__(posicao_x, posicao_y)

        self.sid = sid
        self.direcao_x = direcao_x
        self.direcao_y = direcao_y
        self.raio_bomba = raio_bomba
        self.count_bomba = count_bomba
        self.distancia_bomba = distancia_bomba
        self.angulo_bomba = angulo_bomba

    def criar_bomba(self, x, y, t):
        #Calcula a posição final da bomba
        self.angulo_bomba = math.atan(y/x)
        posicao_final_x = x #int(self.raio_bomba*math.cos(self.angulo_bomba))
        posicao_final_y = y #int(self.raio_bomba*math.sin(self.angulo_bomba))

        bomba = Bomba(posicao_final_x, posicao_final_y, self)
        t.place_bomb(bomba)
        
        '''t = threading.Thread(target=ThreadUpdate.update_bomba, args=(bomba,))
        t.start()
        while t.is_alive():
            pass'''
        
        return True
        
    def andar(self, x, y):
        self.direcao_x = x
        self.direcao_y = y

    def parar_andar(self):
        self.direcao_x = 0
        self.direcao_y = 0
    
    def destruir(self):
        
        personagem = ThreadUpdate.personagens.pop(self.sid)
        
        del personagem