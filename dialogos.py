from colores import rojo, amarillo, verde, rosa, blanco
from gatos import gato
from tiempo import sleep3, sleep
from calculador import suma, resta, multiplicar, dividir, dividir_entero, exponente
from dialogos import error
def error():
  print(rojo + "Respuesta inválida")
  sleep3()
  exit()
mensaje = [
"""                               Me gustaría saber más de ti""", #0
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
"Creo que tal vez porque soy un gato feo...", "La gente en la calle me tiraba cosas y los otros gatos me pegaban y me molestaban mucho, y eso me ponía muy triste :(",#14
"Es difícil vivir sin nadie que te quiera ¿Sabes? Te hace sentir bastante vacío... Y solo...",#15
"Pero ya no quiero hablar más de eso... ¡Lo importante es que ahora vivo aquí y soy más feliz!",#16
"¿Sabes lo feliz que me hace sentir que leas lo que pienso? ¡No puedo ser un gatito más afortunado!",#17
"Tal vez pienses lo contrario, ¡Pero yo creo que eres una muy hermosa persona por disfrutar conocer mi historia de gatito!",#18
"Pocas veces ustedes pueden escucharnos en realidad...",#19
"¡Pero me alegro que ahora sea distinto!", "¿O no?",#20
"Bueno, aunque eso igual no me concierne mucho, pero... ¡Pensaré que eres una persona muy feliz igualmente!",#21
"Digo, ¿Cómo no puedes estarlo? Yo vivo dentro de esta computadora, ¡Pero tú vives en el mundo real!",#22
"¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!", #23
"¿Sabes que dicen que la curiosidad mató al gato no?",#24
"Es una frase muy cruel que dicen ustedes",#25
"¡A mí no me ha matado ninguna curiosidad! ¿Por qué dicen eso?",#26
"Pero admito que soy muy curioso...",#27
# Pregunta de edad 1 30
"¡Pero bueno! Ya sé tu nombre, ehm... ¿Qué edad tienes?\n", #28
"¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!",#29
#condicional pregunta2 1 - opción A 24
"Sé que es algo precipitado pero... ¿Te gustaría ser mi dueño?",#30
"¡No sabes lo feliz que estoy! ¡Prometo ser un buen gato!",#31
"Digo, no solo soy un gato en una computadora que habla... ¡También sé hacer muchas cosas!",#32
"¿Quieres ver?",#33
"Verás, los gatos somos súper inteligentes, pero estando en esta computadora, puedo ser...",#34
"¡AÚN MÁS INTELIGENTE!",#35
"¡Y tengo incluso la capacidad de utilizar la calculadora de esta computadora y resolverte cualquier problema matemático!", #36
#condicional pregunta5 1 - opción A
"¿Quieres probar mi inteligencia?"#37
]
final = [
"Bien, entonces que ya has comprobado mi inteligencia, creo que es hora de...",
"¡Que empieces a estudiar holgazán! ¿Qué haces poniendo a un gato virtual a ayudarte con matemáticas?",
"¡Deberías estar avergonzado! Mejor me voy de vuelta a mi cibercasa y te dejo a tí a reflexionar un rato",
"No sé, busca un libro de matemáticas, busca tu cuaderno, haz algo...",
"¿Sabes qué? Mejor me voy a dormir ¡Ya he hablado demasiado por hoy!"
]
creditos = ["Creado por Alejandro Rondón entre diciembre del 2022 y enero del 2023.",
 "Como proyecto para la facultad de ingeniería de sistemas.", "¡Espero que hayas disfrutado a Intelicat!",
  "¡A él también le gustó mucho tu compañía, estoy seguro que se divirtió muchísimo contigo!",
 "FIN"]
def edad():
    from main import nombre
    edad = input("")
    if edad <= "25":
      sleep()
      print(verde + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida" + gato[5])
  
      sleep()
      print(verde + mensaje[22] + gato[4])
  
      sleep()
      print(blanco + mensaje[23] + gato[4])
  
      sleep()
      print(rosa + mensaje[24] + gato[6])
  
      sleep()
      print(rosa + f"Oh {nombre} tienes una libertad increíble, ¡Debes aprovecharla cada instante! ¡No dejes que nadie te la quite jamás!" + gato[5])
  
      sleep()
      print(blanco + f"Y tampoco dejes la libertad para ser feliz por culpa de nadie, vive tu propia vida {nombre} ¡COMO YO!" + gato[5])
      sleep()
    # Pregunta de edad 1
    elif edad > "25":
      sleep()
      print(verde + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!" + gato[5])
    
      sleep()
      
      print(amarillo + mensaje[25] + gato[6])
    Opcion = input("")
        
    if Opcion == 1:
      suma()
  
    elif Opcion == 2:
      resta()
  
    elif Opcion == 3:
      multiplicar()
  
    elif Opcion == 4:
      dividir()
  
    elif Opcion == 5:
      dividir_entero()
  
    elif Opcion == 6:
      exponente()

    else:
      error()