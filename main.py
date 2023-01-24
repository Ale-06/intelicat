from colores import amarillo, rojo, rosa, verde, blanco, azul
from playsound import playsound
import colorama
from colorama import Fore, Back, Style
import time
from gatos import gato, alternativo
from tiempo import t1, t2, t3, t4
colorama.init()

      # Espacio entre diálogos
espacio = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Menu1 = Fore.WHITE + """



                                  BIENVENIDO A INTELICAT
                               ¿Podrías decirme tu nombre?



"""
import threading
def loopSound():
    while True:
        playsound('C:\\Users\\.\\Desktop\\Codigo, paginas y proyectos\\python\\intelicat\\sounds\\sample.mp3', block=True) # Personalizar la ruta a su conveniencia
        
loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True
loopThread.start()
print(espacio)
print(Menu1)
print(amarillo + Back.RESET + gato[3])

print(Style.RESET_ALL)
nombre =  input(Style.RESET_ALL + "\n").title()
nombremayus = nombre.upper()
t3
print(espacio)
print("                                         ...")
t2
print(espacio)
print(f"""
                                    Oh... {nombre}
                               ¡Ese es un lindo nombre!

""")

print(amarillo + Back.RESET + gato[3])
t3
print(espacio)
print(Style.RESET_ALL + f"""

                                    Sabes {nombre}.....
""")
print(amarillo + Back.RESET + gato[4])
t3
print(espacio)
print("""
                               Me gustaría saber más de ti""")
t3
print(espacio)
print(amarillo + """                    Y como veo que sigues con el programa abierto, tal vez...
                            ¡Tú también quieres que sepa más de tí!
                               """)
print(amarillo + Back.RESET + gato[5])
t2
pregunta1 = input(verde + """
                                          Responde.
                            [¿Qué eres?] - [¿Qué quieres saber de mí?]
                                 (1)                   (2) \n""")
if pregunta1 == "1":
  t1
  print(espacio)
  print(rosa + "Oh... ¡¿QUIERES CONOCERME A MÍ?!")
  print(gato[4])
  t2
  print(espacio)
  print(rosa + "La gente no suele preguntarme eso....")
  print(gato[3])
  t2
  print(espacio)
  print(rosa + "¡Pero ya que insistes!")
  print(gato[6])
  t2
  print(espacio)
  print(rosa + "A ver... ¿Por dónde empiezo?")
  print(gato[3])
  t3
  print(espacio)
  print(rosa + "Bueno, soy un lindo gatito como ya habrás podido darte cuenta!")
  print(gato[5])
  t3
  print(espacio)
  print(rosa + "Fuí creado por un chico universitario, creo que su nombre era ehm.... OH, " + amarillo + "¡Alejandro!")
  print(rosa + gato[5])
  t3
  print(espacio)
  print("¡Él logró rescatarme! Y ahora soy un gatito feliz que vive dentro de esta computadora.")
  print(gato[5])
  t3
  print(espacio)
  print("¡Y estoy muy feliz por eso!")
  print(gato[5])
  t3
  print(espacio)
  print(blanco + "...")
  print(gato[3])
  t3
  print(espacio)
  print(azul + "Antes de vivir aquí, no era un gatito tan feliz... ¿Sabes?")
  print(gato[2])
  t4
  print(espacio)
  print(azul + "Nunca tuve un dueño que me quisiera y me tuviese en su casa, ¡Con una linda cobija y muchos juguetes!")
  print(gato[2])
  t3
  print(espacio)
  print(azul + "Creo que tal vez porque soy un gato feo...")
  print(gato[1])
  t4
  print(espacio)
  print(azul + "La gente en la calle me tiraba cosas y los otros gatos me pegaban y me molestaban mucho, y eso me ponía muy triste :(")
  print(gato[1])
  t4
  print(espacio)
  print(azul + "Es difícil vivir sin nadie que te quiera ¿Sabes? Te hace sentir bastante vacío... Y solo...")
  print(gato[1])
  t4
  print(espacio)
  print(amarillo + "Pero ya no quiero hablar más de eso... ¡Lo importante es que ahora vivo aquí y soy más feliz!")
  print(gato[5])
  t4
  print(espacio)
  print(rosa + "¿Sabes lo feliz que me hace sentir que leas lo que pienso? ¡No puedo ser un gatito más afortunado!")
  print(gato[5])
  t4
  print(espacio)
  print(amarillo + "Tal vez pienses lo contrario, ¡Pero yo creo que eres una muy hermosa persona por disfrutar conocer mi historia de gatito!")
  print(gato[5])
  t3
  print(espacio)
  print(amarillo + "Pocas veces ustedes pueden escucharnos en realidad...")
  print(gato[3])
  t3
  print(espacio)
  print(amarillo + "¡Pero me alegro que ahora sea distinto!")
  print(gato[6])
  t3
  print(espacio)
  print(verde + f"Y bueno {nombre}... Ya que sabes más sobre mí, ¡Ahora es mi turno de preguntarte a ti! ¿Qué edad tienes?")
  print(gato[5])
  edad = input("")
  if edad <= "25":
    t3
    print(espacio)
    print(verde + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida")
    print(gato[5])
    t3
    print(espacio)
    print(verde + f"¿O no?")
    print(gato[4])
    t3
    print(espacio)
    print(blanco + f"Bueno, aunque eso igual no me concierne mucho, pero... ¡Pensaré que eres una persona muy feliz igualmente!")
    print(gato[4])
    t3
    print(espacio)
    print(rosa + f"Digo, ¿Cómo no puedes estarlo? Yo vivo dentro de esta computadora, ¡Pero tú vives en el mundo real!")
    print(gato[6])
    t3
    print(espacio)
    print(rosa + f"Oh {nombre} tienes una libertad increíble, ¡Debes aprovecharla cada instante! ¡No dejes que nadie te la quite jamás!")
    print(gato[5])
    t3
    print(espacio)
    print(blanco + f"Y tampoco dejes la libertad para ser feliz por culpa de nadie, vive tu propia vida {nombre} ¡COMO YO!")
    print(gato[5])
    t3
  elif edad > "25":
    t3
    print(espacio)
    print(verde + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!")
    print(gato[5])
    t4
    print(espacio)
    print(amarillo + f"¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!")
    print(gato[6])
elif pregunta1 == "2":
  t1
  print(espacio)
  print(rosa + "¿Sabes que dicen que la curiosidad mató al gato no?")
  print(gato[4])
  t3
  print(espacio)
  print(rojo + "Es una frase muy cruel que dicen ustedes")
  print(gato[0])
  t3
  print(espacio)
  print(rojo + "¡A mí no me ha matado ninguna curiosidad! ¿Por qué dicen eso?")
  print(gato[0])
  t3
  print(espacio)
  print(azul + "Pero admito que soy muy curioso...")
  print(gato[9])
  t3
  print(espacio)
  print(verde + "¡Pero bueno! Ya sé tu nombre, ehm... ¿Qué edad tienes?\n")
  print(gato[4])
  edad = input("")
  if edad <= "25":
    t3
    print(espacio)
    print(verde + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida")
    print(gato[5])
    t3
  elif edad > "25":
    t3
    print(espacio)
    print(verde + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!")
    print(gato[5])
    t4
    print(espacio)
    print(amarillo + f"¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!")
    print(gato[6])
    t4
else:
  print(espacio)
  print(rojo + "Respuesta inválida")
  t3
  exit()
print(espacio)
print(verde + f"Sabes... ¡Me caes demasiado bien {nombre}!")
print(gato[4])
t3
print(espacio)
print(amarillo + f"Sé que es algo precipitado pero... ¿Te gustaría ser mi dueño?")
print(gato[7])
t1
pregunta2 = input(verde + """
                                              Responde.
                            [¡Claro que si!]      -      [No.]
                                   (1)                    (2) \n""")
if pregunta2 == "1":
  t3
  print(espacio)
  print(rosa + "¡¡¿¡EN SERIOOOO?!!? NO SÉ QUE DECIR ESTOY DEMASIADO FELIZ OMG")
  print(gato[7])
  t3
  print(espacio)
  print(rosa + "TE")
  print(gato[7])
  t1
  print(espacio)
  print(rosa + "AMO")
  print(gato[7])
  t1
  print(espacio)
  print(rosa + "DEMASIADO")
  print(gato[8])
  t1
  print(espacio)
  print(rosa + "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  print(gato[8])
  t1
  print(espacio)
  print(rosa + "Perdona el ataque de emoción, ya me calmo...")
  print(gato[6])
  t3
  print(espacio)
  print(amarillo + "Es que, ¡Al fin tengo un dueño! ¡Es la primera vez que tengo uno!")
  print(gato[7])
  t3
  print(espacio)
  print(amarillo + "Bien ehm... ¿Qué sigue? ¡OH SI YA SÉ!")
  print(gato[4])
  t3
  print(espacio)
  print(rosa + "¿Qué nombre te gustaría ponerme? \n")
  print(gato[4])
  namecat = input("")
  namecatmayus = namecat.upper()
  t2
  print(espacio)
  print(amarillo + f"OH {namecatmayus} ¡QUE LINDO NOMBRE GRACIAS {nombremayus}!")
  print(gato[4])
  t3
  print(espacio)
  print(rosa + f"¡No sabes lo feliz que estoy! ¡Prometo ser un buen gato!")
  print(gato[8])
  t3
  print(espacio)
  print(rosa + f"¡No sabes lo feliz que estoy! ¡Prometo ser un buen gato!")
  print(gato[7])
#continuar
if pregunta2 == "2":
  def loopSound():
    while True:
        playsound('C:\\Users\\.\\Desktop\\Codigo, paginas y proyectos\\python\\intelicat\\sounds\\angry.mp3', block=True) # Personalizar la ruta a su conveniencia
  loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
  loopThread.daemon = True 
  loopThread.start()
  t1
  print(espacio)
  print(rojo + f"¿QUÉ?")
  print(gato[0])
  t2
  print(espacio)
  print(rojo + f"¡¿¡CÓMO QUE NO!? QUÉ HE HECHO MAL PARA QUE NO QUIERAS ADOPTARME {nombremayus}!")
  print(gato[0])
  t3
  print(espacio)
  print(rojo + f"¿ACASO ME ODIAS {nombremayus}?")
  print(gato[0])
  t1
  pregunta3 = input(verde + """
                                              Responde.
                            [¡Claro que si!]      -      [No.]
                                   (1)                    (2) \n""")
  if pregunta3 == "1" or "2":
    print(espacio)
    t1
    print(rojo + "¿QUÉ?")
    t1
    print(rojo + "¡NO!")
    t1
    print(rojo + "TU")
    t1
    print(rojo + "MIENTES")
    t1
    print(espacio)
    print(rojo + f"SÉ LO QUE PIENSAS {nombremayus}")
    t3
    print(espacio)
    print(rojo + "ERES")
    t1
    print(espacio)
    print(rojo + "UNA")
    t1
    print(espacio)
    print(rojo + "MALA")
    t1
    print(espacio)
    print(rojo + "PERSONA")
    t1
    print(espacio)
    print(rojo + ".")
    t1
    print(espacio)
    print(rojo + "..")
    t1
    print(espacio)
    print(rojo + "...")
    t3
    print(alternativo[0])
  else:
    print(espacio)
    print(rojo + "Respuesta inválida")
    t3
    exit()