from tablero import Tablero
from jugador import Jugador,Adivina,CreaCodigo


class JuegoPrincipal:
    def __init__(self) -> None:
        self.tablero = Tablero()
        self.adivina = None
        self.crea_codigo = None
        
        
    # metodo inicializacion del juego
    
    def inicio(self):
        jugador_input = input("Eres creador o adivinador")
        
        if jugador_input == 'creador':
         self.crea_codigo = CreaCodigo(persona=True)
         self.adivina = Adivina(persona=False)
        elif jugador_input == 'adivinador':
            self.crea_codigo = CreaCodigo(persona=False)
            self.adivina = Adivina(persona=True)
        else: 
            print("Error digite correctamnte palabra")
            return 
        self.tablero.definir_color(self.crea_codigo.obtener_codigo())
        
    def juego(self):
        if self.crea_codigo is None or self.adivina is None:
            print("defina jugador")
            return
        
        for i in range(12):
            intento = self.adivina.obtener_codigo()
            retroalimentacion = self.tablero.validar_ganador(intento)
            self.tablero.actualiza(intento,retroalimentacion)
            self.tablero.mostrar()
            
            
        

