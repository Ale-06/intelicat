from colores import rojo, amarillo, verde, rosa, blanco
from gatos import gato
from tiempo import sleep3, espacio, sleep, sleep1
from calculador import suma, resta, multiplicar, dividir, dividir_entero, exponente
def error():
  print(rojo + "Respuesta inválida")
  sleep3()
  exit()
mensaje = ["""                               Me gustaría saber más de ti""", #0
#condicional pregunta1 1 - opción A
"""                    Y como veo que sigues con el programa abierto, tal vez...
                            ¡Tú también quieres que sepa más de tí!""",#1
"Oh... ¡¿QUIERES CONOCERME A MÍ?!",#2
"La gente no suele preguntarme eso....",#3
"¡Pero ya que insistes!",#4
"A ver... ¿Por dónde empiezo?",#5
"Bueno, soy un lindo gatito como ya habrás podido darte cuenta!",#6
"Fuí creado por un chico universitario, creo que su nombre era ehm.... OH, ",#7
"¡Alejandro!",#8
"¡Él logró rescatarme! Y ahora soy un gatito feliz que vive dentro de esta computadora.",#9
"¡Y estoy muy feliz por eso!",#10
"...",#11
"Antes de vivir aquí, no era un gatito tan feliz... ¿Sabes?",#12
"Nunca tuve un dueño que me quisiera y me tuviese en su casa, ¡Con una linda cobija y muchos juguetes!",#13
"Creo que tal vez porque soy un gato feo...", #14
"La gente en la calle me tiraba cosas y los otros gatos me pegaban y me molestaban mucho, y eso me ponía muy triste :(",#15
"Es difícil vivir sin nadie que te quiera ¿Sabes? Te hace sentir bastante vacío... Y solo...",#16
"Pero ya no quiero hablar más de eso... ¡Lo importante es que ahora vivo aquí y soy más feliz!",#17
"¿Sabes lo feliz que me hace sentir que leas lo que pienso? ¡No puedo ser un gatito más afortunado!",#18
"Tal vez pienses lo contrario, ¡Pero yo creo que eres una muy hermosa persona por disfrutar conocer mi historia de gatito!",#19
"Pocas veces ustedes pueden escucharnos en realidad...",#20
"¡Pero me alegro que ahora sea distinto!", #21
#condicional pregunta1 2 - opción B
"¿Sabes que dicen que la curiosidad mató al gato no?", #22
#Respuesta
"Es una frase muy cruel que dicen ustedes",#23
"¡A mí no me ha matado ninguna curiosidad! ¿Por qué dicen eso?",#24
"Pero admito que soy muy curioso...",#25
# Pregunta de edad 1 
"¡Pero bueno! Ya sé tu nombre, ehm... ¿Qué edad tienes?\n", #26
#condicional pregunta2 1 - opción A 
"Sé que es algo precipitado pero... ¿Te gustaría ser mi dueño?",#27
#Respuesta
"¡¡¿¡EN SERIOOOO?!!? NO SÉ QUE DECIR ESTOY DEMASIADO FELIZ OMG", #28
"TE", #29
"AMO", #30
"DEMASIADO", #31
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", #32
"Perdona el ataque de emoción, ya me calmo...", #33
"Es que, ¡Al fin tengo un dueño! ¡Es la primera vez que tengo uno!", #34
"Bien ehm... ¿Qué sigue? ¡OH SI YA SÉ!", #35
# Pregunta nombre gato
"¿Qué nombre te gustaría ponerme? \n", #36
#Respuesta
"¡No sabes lo feliz que estoy! ¡Prometo ser un buen gato!",#37
"Digo, no solo soy un gato en una computadora que habla... ¡También sé hacer muchas cosas!",#38
#condicional pregunta4 1 - opción A 
"¿Quieres ver?",#39
#Respuesta
"Verás, los gatos somos súper inteligentes, pero estando en esta computadora, puedo ser...",#40
"¡AÚN MÁS INTELIGENTE!",#41
"¡Y tengo incluso la capacidad de utilizar la calculadora de esta computadora y resolverte cualquier problema matemático!", #42
#condicional pregunta5 1 - opción A 

"¿Quieres probar mi inteligencia?"#43
]
final = [
"Bien, entonces ya que has comprobado mi inteligencia, creo que es hora de...",
"¡Que empieces a estudiar holgazán! ¿Qué haces poniendo a un gato virtual a ayudarte con matemáticas?",
"¡Deberías estar avergonzado! Mejor me voy de vuelta a mi cibercasa y te dejo a tí a reflexionar un rato",
"No sé, busca un libro de matemáticas, busca tu cuaderno, haz algo...",
"¿Sabes qué? Mejor me voy a dormir ¡Ya he hablado demasiado por hoy!"
]
creditos = ["Creado por Alejandro Rondón entre diciembre del 2022 y enero del 2023.",
 "Como proyecto para la facultad de ingeniería de sistemas.", "¡Espero que hayas disfrutado a Intelicat!",
  "¡A él también le gustó mucho tu compañía, estoy seguro que se divirtió muchísimo contigo!",
 "                                                        FIN"]
def Menu1():
  Menu1 = blanco + """



                                         BIENVENIDO A INTELICAT
                                      ¿Podrías decirme tu nombre?



  """

  espacio()
  print(Menu1)
  print(amarillo + gato[3])



def calculadora2():
    Opcion = input("")
        
    if Opcion == "1":
      suma()
  
    elif Opcion == "2":
      resta()
  
    elif Opcion == "3":
      multiplicar()
  
    elif Opcion == "4":
      dividir()
  
    elif Opcion == "5":
      dividir_entero()
  
    elif Opcion == "6":
      exponente()

    else:
      error()