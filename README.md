# mastemind

EXPLICACION DE CODIGO:
Se crearon 3 archivos donde cada uno recibe el nombre :
-Tablero : La clase Tablero organiza un juego en el que un jugador adivina una combinación de colores. Permite definir la combinación secreta, validar los intentos del jugador, mostrar los resultados y actualizar la lista de intentos y retroalimentación. ¡Es una manera ordenada de manejar el juego y proporcionar una experiencia interactiva!

-Jugador: El jugador es la base para los jugadores del juego, definiendo los colores disponibles y si el jugador es una persona real o una máquina.
Adivina es el jugador que intenta adivinar el código. Puede ingresar un código manualmente o generar uno al azar si es una máquina.
CreaCodigo es el jugador que crea el código secreto. Similar a Adivina, puede ingresar un código manualmente o generar uno al azar si es una máquina.

-Juego principal: Es la clase que maneja el juego completo.
Permite a un jugador elegir entre ser el creador del código o el adivinador.
El juego da al adivinador hasta 12 intentos para adivinar el código secreto creado por el creador.
Muestra retroalimentación y actualiza el estado del juego después de cada intento.
Anuncia si el jugador gana o pierde después de los intentos.

CLASES  --> 
1-  Class jugador :
 Defini una variable global llamada "tamano_codigo" que tiene un valor de 4 y esto representaria que la lista se manejaria de 4 colores.

 -Dentro de la clase jugador definimos una funcion "def_init_(self,persona=true):" al usar en _unit_ estamos creando un nuevo objecto dentro de la clase ,donde mandamos como parametro persona y por defecto colocamos que es true .

 -se guarda el valor de persona en el atributo persona del objeto para saber si el codigo ingresado es una persona o el codigo se genera aleatorio.

 Class Adivina :
 se crea una nueva clase "adivina" que va heredar la clase jugador"padre" . Al heredar jugador en la clase adivina tendria acceso a todos los atributos y metodos de la clase padre.

 - se creo un metodo llamado obtener codigo 
 - se realiza la verificacion que si persona es true entonces el codigo sera ingresado por la persona
 - codigo es igual input donde muestra en la consola  un mensje y espera que el usuario escriba alg.utilizamos strip para eliminar espacios al principio y final del texto y el split pra dividir el texto en una lista de palabras ,usando los espacios como separadores
-hacemos un else si persona es false entoncs el codigo es generado aleatoriamente. usamos el la funcion choices ddel modulo random para selecionar al azar el tamano de codigo de la lista de colores.
el resultado es una lista de colores aleatorios.
- se hace un return de codigo que devuelve el codigo ya ingresado por una persona o aleatorio

Class CreaCodigo:
- A esta clase igual se le hereda la clase padre jugador
-se define el metodo obtener codigo
-el crear codigo tiene el mismo comportamiento que hace la clase adivinador 
-hacemos una verificacion donde si persona es true pide al usuario que ingrese un codigo de 4 colores y si la persona es false se genera un codigo aleatorio de 4 colores
-y por ultimo hacemos un return de codigo que devuelve el codigo obtenido


2-Class  Tablero :
-Importación de Herramientas para Colores -->Herramienta de una biblioteca llamada colored que permiten cambiar el color del texto en la pantalla. Cuando mostramos los colores o los resultados, podemos verlos en colores bonitos en la terminal.
-Definir la Clase Tablero
-Se crea un diccionario de los Colores --> Es una lista con la que vamos asociar los nombres de los colores con el códigos que hacen que el texto aparezca de color en la pantalla. 
-Se creo el método constructor--> Inicializacion del tablero en dos cosas:
color_secreto: Un lugar donde guardaremos la combinación de colores que el jugador debe adivinar.
turnos: Una lista que guardará todos los intentos del jugador y cómo le fue con cada uno.
-Definir el Color Secreto--> Establecer la combinación de colores que el jugador tiene que adivinar. Guardamos esa combinación en color_secreto.
- Validar el Intento del Jugador--> Se compara el intento del jugador con la combinación secreta.
Si un color está en la posición correcta, se dice que el color es "verde".
Si un color está en la combinación secreta pero en la posición incorrecta, se dice que el color es "amarillo".
Si el color no está en la combinación secreta, se dice que el color es "blanco".
retroalimentacion es una lista que guarda estos resultados para cada color en el intento del jugador.
-Mostrar Resultados en la Pantalla --> En la pantalla  se mostraran todos los intentos que el jugador ha hecho y cómo le fue con cada intento.
 En la fila_color muestra los colores del intento del jugador.
En la fila_retroalimentacion muestra si cada color en el intento fue verde, amarillo o blanco.
Los colores y los resultados se muestran en la pantalla uno al lado del otro.
-Actualizar el Tablero con un Nuevo Intento --> Agrega un nuevo intento del jugador y la retroalimentación a la lista de turnos. Esto permite mantener un registro de todos los intentos hechos y cómo se ha respondido a cada uno.

3-Class juego_principal:
-Importación de Módulos " las clases Tablero, Adivina y CreaCodigo"
-Definición de la Clase JuegoPrincipal
-Se crea el método constructor--> self.tablero: Crea una nueva instancia del Tablero para gestionar el juego.
self.adivina y self.crea_codigo: Inicialmente no tienen valor (None). Estos se asignarán más adelante según el rol del jugador.
-Método de Inicio del Juego--> Pide al jugador que elija su rol:
Si elige "creador", se crea un objeto CreaCodigo para crear el código secreto y un objeto Adivina para adivinar el código.
Si elige "adivinador", se crea un objeto CreaCodigo para crear el código secreto y un objeto Adivina para adivinar el código.
Si la entrada no es válida, muestra un mensaje de error.
Luego, usa self.crea_codigo.obtener_codigo() para obtener el código secreto y lo configura en el tablero.
-Método de Ejecución Principal del Juego--> Ejecuta el juego de adivinanza:
Ciclo de intentos: Permite hasta 12 intentos para adivinar el código secreto.
Obtener intento: Usa self.adivina.obtener_codigo() para que el jugador haga un intento.
Validar intento: Usa self.tablero.validar_ganador(intento) para obtener retroalimentación sobre el intento.
Actualizar tablero: Agrega el intento y la retroalimentación al tablero.
Mostrar estado: Muestra el estado actual del tablero.
Verificar victoria: Si la retroalimentación indica que todos los colores son correctos colorr verde  * 4, imprime un mensaje de victoria y termina el juego.
Verificar derrota: Si se agotaron los 12 intentos sin adivinar el código, imprime un mensaje de derrota y muestra el código secreto.
-Iniciar el Juego --> Crea una instancia del juego y lo inicia:
jugar = JuegoPrincipal(): Crea un nuevo juego.
jugar.inicio(): Llama al método inicio para configurar el juego.
jugar.ejecucion_principal(): Comienza a ejecutar el juego, permitiendo que el jugador intente adivinar el código.