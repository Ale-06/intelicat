from colores import amarillo, rojo, rosa, verde, blanco, azul
from playsound import playsound
import colorama
from colorama import Fore, Style
from gatos import gato, alternativo
from tiempo import sleep1, sleep2, sleep3, sleep4, sleep10, espacio
from preguntas import question1, question2
import threading
def loopSound():
    while True:
        playsound('\\sounds\\sample.mp3', block=True) # Personalizar la ruta a su conveniencia

loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True
loopThread.start()
colorama.init()

Menu1 = Fore.WHITE + """



                                  BIENVENIDO A INTELICAT
                               ¿Podrías decirme tu nombre?



"""

espacio()
print(Menu1)
print(amarillo + gato[3])

print(Style.RESET_ALL)
nombre =  input(Style.RESET_ALL + "\n").title()
nombremayus = nombre.upper()

 
print("                                         ...")
sleep2()
 
print(f"""
                                    Oh... {nombre}
                               ¡Ese es un lindo nombre!

""")

print(amarillo + gato[3])
sleep3()
 
print(Style.RESET_ALL + f"""

                                    Sabes {nombre}.....
""")
print(amarillo + gato[4])
sleep3()
 
print("""
                               Me gustaría saber más de ti""")
sleep3()
 
print(amarillo + """                    Y como veo que sigues con el programa abierto, tal vez...
                            ¡Tú también quieres que sepa más de tí!
                               """)
print(amarillo + gato[5])
sleep10()
question1()
pregunta1 = input("")
if pregunta1 == "1":
  sleep1()
   
  print(rosa + "Oh... ¡¿QUIERES CONOCERME A MÍ?!")
  print(gato[4])
  sleep2()
   
  print(rosa + "La gente no suele preguntarme eso....")
  print(gato[3])
  sleep2()
   
  print(rosa + "¡Pero ya que insistes!")
  print(gato[6])
  sleep2()
   
  print(rosa + "A ver... ¿Por dónde empiezo?")
  print(gato[3])
  sleep3()
   
  print(rosa + "Bueno, soy un lindo gatito como ya habrás podido darte cuenta!")
  print(gato[5])
  sleep3()
   
  print(rosa + "Fuí creado por un chico universitario, creo que su nombre era ehm.... OH, " + amarillo + "¡Alejandro!")
  print(rosa + gato[5])
  sleep3()
   
  print("¡Él logró rescatarme! Y ahora soy un gatito feliz que vive dentro de esta computadora.")
  print(gato[5])
  sleep3()
   
  print("¡Y estoy muy feliz por eso!")
  print(gato[5])
  sleep3()
   
  print(blanco + "...")
  print(gato[3])
  sleep3()
   
  print(azul + "Antes de vivir aquí, no era un gatito tan feliz... ¿Sabes?")
  print(gato[2])
  sleep4()
   
  print(azul + "Nunca tuve un dueño que me quisiera y me tuviese en su casa, ¡Con una linda cobija y muchos juguetes!")
  print(gato[2])
  sleep3()
   
  print(azul + "Creo que tal vez porque soy un gato feo...")
  print(gato[1])
  sleep4()
   
  print(azul + "La gente en la calle me tiraba cosas y los otros gatos me pegaban y me molestaban mucho, y eso me ponía muy triste :(")
  print(gato[1])
  sleep4()
   
  print(azul + "Es difícil vivir sin nadie que te quiera ¿Sabes? Te hace sentir bastante vacío... Y solo...")
  print(gato[1])
  sleep4()
   
  print(amarillo + "Pero ya no quiero hablar más de eso... ¡Lo importante es que ahora vivo aquí y soy más feliz!")
  print(gato[5])
  sleep4()
   
  print(rosa + "¿Sabes lo feliz que me hace sentir que leas lo que pienso? ¡No puedo ser un gatito más afortunado!")
  print(gato[5])
  sleep4()
   
  print(amarillo + "Tal vez pienses lo contrario, ¡Pero yo creo que eres una muy hermosa persona por disfrutar conocer mi historia de gatito!")
  print(gato[5])
  sleep3()
   
  print(amarillo + "Pocas veces ustedes pueden escucharnos en realidad...")
  print(gato[3])
  sleep3()
   
  print(amarillo + "¡Pero me alegro que ahora sea distinto!")
  print(gato[6])
  sleep3()
   
  print(verde + f"Y bueno {nombre}... Ya que sabes más sobre mí, ¡Ahora es mi turno de preguntarte a ti! ¿Qué edad tienes?")
  print(gato[5])
  edad = input("")
  if edad <= "25":
    sleep3()
     
    print(verde + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida")
    print(gato[5])
    sleep3()
     
    print(verde + f"¿O no?")
    print(gato[4])
    sleep3()
     
    print(blanco + f"Bueno, aunque eso igual no me concierne mucho, pero... ¡Pensaré que eres una persona muy feliz igualmente!")
    print(gato[4])
    sleep3()
     
    print(rosa + f"Digo, ¿Cómo no puedes estarlo? Yo vivo dentro de esta computadora, ¡Pero tú vives en el mundo real!")
    print(gato[6])
    sleep3()
     
    print(rosa + f"Oh {nombre} tienes una libertad increíble, ¡Debes aprovecharla cada instante! ¡No dejes que nadie te la quite jamás!")
    print(gato[5])
    sleep3()
     
    print(blanco + f"Y tampoco dejes la libertad para ser feliz por culpa de nadie, vive tu propia vida {nombre} ¡COMO YO!")
    print(gato[5])
    sleep3()
  elif edad > "25":
    sleep3()
     
    print(verde + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!")
    print(gato[5])
    sleep4()
     
    print(amarillo + f"¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!")
    print(gato[6])
elif pregunta1 == "2":
  sleep1()
   
  print(rosa + "¿Sabes que dicen que la curiosidad mató al gato no?")
  print(gato[4])
  sleep3()
   
  print(rojo + "Es una frase muy cruel que dicen ustedes")
  print(gato[0])
  sleep3()
   
  print(rojo + "¡A mí no me ha matado ninguna curiosidad! ¿Por qué dicen eso?")
  print(gato[0])
  sleep3()
   
  print(azul + "Pero admito que soy muy curioso...")
  print(gato[9])
  sleep3()
   
  print(verde + "¡Pero bueno! Ya sé tu nombre, ehm... ¿Qué edad tienes?\n")
  print(gato[4])
  edad = input("")
  if edad <= "25":
    sleep3()
     
    print(verde + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida")
    print(gato[5])
    sleep3()
  elif edad > "25":
    sleep3()
     
    print(verde + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!")
    print(gato[5])
    sleep4()
     
    print(amarillo + f"¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!")
    print(gato[6])
    sleep4()
else:
   
  print(rojo + "Respuesta inválida")
  sleep3()
  exit()
 
print(verde + f"Sabes... ¡Me caes demasiado bien {nombre}!")
print(gato[4])
sleep3()
 
print(amarillo + f"Sé que es algo precipitado pero... ¿Te gustaría ser mi dueño?")
print(gato[7])
sleep10()
question2()
pregunta2 = input("")
if pregunta2 == "1":
  sleep3()
   
  print(rosa + "¡¡¿¡EN SERIOOOO?!!? NO SÉ QUE DECIR ESTOY DEMASIADO FELIZ OMG")
  print(gato[7])
  sleep3()
   
  print(rosa + "TE")
  print(gato[7])
  sleep1()
   
  print(rosa + "AMO")
  print(gato[7])
  sleep1()
   
  print(rosa + "DEMASIADO")
  print(gato[8])
  sleep1()
   
  print(rosa + "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  print(gato[8])
  sleep1()
   
  print(rosa + "Perdona el ataque de emoción, ya me calmo...")
  print(gato[6])
  sleep3()
   
  print(amarillo + "Es que, ¡Al fin tengo un dueño! ¡Es la primera vez que tengo uno!")
  print(gato[7])
  sleep3()
   
  print(amarillo + "Bien ehm... ¿Qué sigue? ¡OH SI YA SÉ!")
  print(gato[4])
  sleep3()
   
  print(rosa + "¿Qué nombre te gustaría ponerme? \n")
  print(gato[4])
  namecat = input("")
  namecatmayus = namecat.upper()
  sleep2()
   
  print(amarillo + f"OH {namecatmayus} ¡QUE LINDO NOMBRE GRACIAS {nombremayus}!")
  print(gato[4])
  sleep3()
   
  print(rosa + f"¡No sabes lo feliz que estoy! ¡Prometo ser un buen gato!")
  print(gato[8])
  sleep3()
   
  print(rosa + f"¡No sabes lo feliz que estoy! ¡Prometo ser un buen gato!")
  print(gato[7])
#continuar
if pregunta2 == "2":
  def loopSound():
    while True:
        playsound('\\sounds\\angry.mp3', block=True) # Personalizar la ruta a su conveniencia
  loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
  loopThread.daemon = True 
  loopThread.start()
  sleep1()
   
  print(rojo + f"¿QUÉ?")
  print(gato[0])
  sleep2()
   
  print(rojo + f"¡¿¡CÓMO QUE NO!? QUÉ HE HECHO MAL PARA QUE NO QUIERAS ADOPTARME {nombremayus}!")
  print(gato[0])
  sleep3()
   
  print(rojo + f"¿ACASO ME ODIAS {nombremayus}?")
  print(gato[0])
  sleep10()
  question2()
  pregunta3 = ("")
  if pregunta3 == "1" or "2":
     
    sleep1()
    print(rojo + "¿QUÉ?")
    sleep1()
    print(rojo + "¡NO!")
    sleep1()
    print(rojo + "TU")
    sleep1()
    print(rojo + "MIENTES")
    sleep1()
     
    print(rojo + f"SÉ LO QUE PIENSAS {nombremayus}")
    sleep3()
     
    print(rojo + "ERES")
    sleep1()
     
    print(rojo + "UNA")
    sleep1()
     
    print(rojo + "MALA")
    sleep1()
     
    print(rojo + "PERSONA")
    sleep1()
     
    print(rojo + ".")
    sleep1()
     
    print(rojo + "..")
    sleep1()
     
    print(rojo + "...")
    sleep3()
    print(alternativo[0])
  else:
     
    print(rojo + "Respuesta inválida")
    sleep3()
    exit()
