from tablero import Tablero
from jugador import Adivina,CreaCodigo


class JuegoPrincipal:
    def __init__(self):
        self.tablero = Tablero()
        self.adivina = None
        self.crea_codigo = None
        
        
    # metodo inicializacion del juego
    
    def inicio(self):
        jugador_input = input("Eres creador o adivinador: ")
        if jugador_input == 'creador':
         self.crea_codigo = CreaCodigo(persona=True)
         self.adivina = Adivina(persona=False)
        elif jugador_input == 'adivinador':
            self.crea_codigo = CreaCodigo(persona=False)
            self.adivina = Adivina(persona=True)
        else: 
            print("Error digite correctamente palabra")
            return 
        self.tablero.definir_color(self.crea_codigo.obtener_codigo())
        
        
    def ejecucion_principal(self):
        for i in range(12):
            intento = self.adivina.obtener_codigo()
            print(intento)
            retroalimentacion = self.tablero.validar_ganador(intento)
            print(retroalimentacion)
            self.tablero.actualiza(intento,retroalimentacion)
            self.tablero.mostrar()
            
            if retroalimentacion==["color_verde"]*4:
                print(" FELICIDADES,HAZ GANADO")
                return
        
        print(f"HAZ PERDIDO,VUELVE A INTENTARLO el codigo era {self.tablero.color_secreto}")
            

    

jugar = JuegoPrincipal() 
jugar.inicio() 
jugar.ejecucion_principal()  


