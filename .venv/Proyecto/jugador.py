import random 

tamano_codigo = 4

class Jugador:
    colores = ["rojo","verde","amarillo","azul"]
    def __init__(self,persona=True):
        self.persona = persona
        
        
class Adivina(Jugador):
    def obtener_codigo(self):
        if self.persona:
            codigo = input('Inserte el codigo de 4 colores (amarrillo,rojo,verde,azul):').strip().split()
        else:
            codigo = random.choices(self.colores, k=tamano_codigo)
        
        return codigo
        
class CreaCodigo(Jugador):
    def obtener_codigo(self):
        if self.persona:
            codigo = input('Inserte el codigo de 4 colores (amarrillo,rojo,verde,azul):').strip().split()
        else:
            codigo = random.choices(self.colores, k=tamano_codigo)
        
        return codigo
            
        
    