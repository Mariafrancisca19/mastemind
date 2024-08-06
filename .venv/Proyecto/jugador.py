import random 

colores = ["rojo","verde","amarillo","azul"]
tamano_codigo = 4

class Jugador:
    def __init__(self,persona=True):
        self.persona = persona
        
        
class Adivina(Jugador):
    def obtener_codigo(self):
        if self.persona:
            codigo = input('Insete el codigo de 4 colores (amarrillo,rojo,verde,azul):').strip().split()
            return codigo.split(',')
        else:
            return random.choices(colores, k=tamano_codigo)
        
        
class CreaCodigo(Jugador):
    def obtener_codigo(self):
        if self.persona:
             codigo = input('Insete el codigo de 4 colores (amarrillo,rojo,verde,azul):').strip().split()
             return codigo.split(',')
        else:
            return random.choices(colores, k=tamano_codigo)
        
            
        
    