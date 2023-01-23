from playsound import playsound
import colorama
from colorama import Fore, Back, Style
import time
colorama.init()
espacio = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
alternativo = ["""
         .    ,,,,,            ,,,,,     .
        .        \.\          /./         .
       .   .__....\.\        /./.....__,   .
      .     .": o :':        ;': o :".      .
     .      `. `-' .'.      .'. `-' .'       .
    .         `---'            `---'          .
   .                                           `
  `  _...----...      ...   ...      ...----..._
 .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
'.-'   _.--"."'       `-._.-'       '.".--._   `-.`
'  .-"'                  :                  `"-.  `
  '   `.              _.'"'._              .'   `
        `.       ,.-'"       "'-.,       .'
          `.                           .'
            `-._                   _.-'
                `"'--...___...--'"` """
                , """
         .    ,,,,,            ,,,,,     .
        .        \.\          /./         .
       .   .__....\.\        /./.....__,   .
      .     .": o :':        ;': o :".      .
     .      `. `-' .'.      .'. `-' .'       .
    .         `---'            `---'          .
   .                                           `
  `  _...----...      ...   ...      ...----..._
 .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
'.-'   _.--"."'       `-._.-'       '.".--._   `-.`
'  .-"'                  :                  `"-.  `
  '   `.              _.'"'._               .'   `
        `.       ,.-'".      ."'-.,       .'
          `.           '-..-'          ,.'
            `-._                   _.-'
                `"'--...___...--'"` """]
gato = ["""
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = I I =_______    \ \  
                                                      \/   \  O      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#0
,"""
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = _ _ =_______    \ \  
                                                      \/   \  ︵      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#1
, """
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = o o =_______    \ \  
                                                      \/   \  ︵      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#2
, """
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = _ _ =_______    \ \  
                                                      \/   \  -      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#3
, """
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = o o =_______    \ \  
                                                      \/   \  -      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#4
, """
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = ^ ^ =_______    \ \  
                                                      \/   \  O      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#5
, """
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = ^ ^ =_______    \ \  
                                                      \/   \  W      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#6
, """
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = O O =_______    \ \  
                                                      \/   \  W      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#7
, """
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = > < =_______    \ \  
                                                      \/   \  W      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#8
, """
___________________________________________________  ________________________________________________________
                                                   \ \ 
                                                    \ \_    /\_/\            ___
                                                     \     = 7 7 =_______    \ \  
                                                      \/   \  -      __(  \.__) )
                                                        (@)<_____>__(_____)____/
\n\n"""
#9
]
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

print(Menu1)
print(Fore.YELLOW + Style.BRIGHT + Back.RESET + gato[3])


print(Style.RESET_ALL)
nombre =  input(Style.RESET_ALL + "\n").title()
nombremayus = nombre.upper()
time.sleep(1)
print(espacio)
print("                                         ...")
time.sleep(1)
print(espacio)
print(f"""
                                    Oh... {nombre}
                               ¡Ese es un lindo nombre!

""")
print(Fore.YELLOW + Style.BRIGHT + Back.RESET + gato[3])
time.sleep(3)
print(espacio)
print(Style.RESET_ALL + f"""

                                    Sabes {nombre}.....
""")
print(Fore.YELLOW + Style.BRIGHT + Back.RESET + gato[4])
time.sleep(3)
print(espacio)
print("""
                               Me gustaría saber más de ti""")
time.sleep(3)
print(espacio)
print(Fore.YELLOW + Style.BRIGHT + """                    Y como veo que sigues con el programa abierto, tal vez...
                            ¡Tú también quieres que sepa más de tí!
                               """)
print(Fore.YELLOW + Style.BRIGHT + Back.RESET + gato[5])
time.sleep(2)
pregunta1 = input(Fore.GREEN + Style.BRIGHT + """
                                          Responde.
                            [¿Qué eres?] - [¿Qué quieres saber de mí?]
                                 (1)                   (2) \n""")
if pregunta1 == "1":
  time.sleep(1)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "Oh... ¡¿QUIERES CONOCERME A MÍ?!")
  print(gato[4])
  time.sleep(2)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "La gente no suele preguntarme eso....")
  print(gato[3])
  time.sleep(2)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "¡Pero ya que insistes!")
  print(gato[6])
  time.sleep(2)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "A ver... ¿Por dónde empiezo?")
  print(gato[3])
  time.sleep(3)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "Bueno, soy un lindo gatito como ya habrás podido darte cuenta!")
  print(gato[5])
  time.sleep(3.5)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "Fuí creado por un chico universitario, creo que su nombre era ehm.... OH, " + Fore.YELLOW + Style.BRIGHT + "¡Alejandro!")
  print(Fore.MAGENTA + Style.BRIGHT + gato[5])
  time.sleep(3)
  print(espacio)
  print("¡Él logró rescatarme! Y ahora soy un gatito feliz que vive dentro de esta computadora.")
  print(gato[5])
  time.sleep(3)
  print(espacio)
  print("¡Y estoy muy feliz por eso!")
  print(gato[5])
  time.sleep(3)
  print(espacio)
  print(Fore.WHITE + Style.BRIGHT + "...")
  print(gato[3])
  time.sleep(3)
  print(espacio)
  print(Fore.CYAN + Style.BRIGHT + "Antes de vivir aquí, no era un gatito tan feliz... ¿Sabes?")
  print(gato[2])
  time.sleep(4)
  print(espacio)
  print(Fore.CYAN + Style.BRIGHT + "Nunca tuve un dueño que me quisiera y me tuviese en su casa, ¡Con una linda cobija y muchos juguetes!")
  print(gato[2])
  time.sleep(3)
  print(espacio)
  print(Fore.CYAN + Style.BRIGHT + "Creo que tal vez porque soy un gato feo...")
  print(gato[1])
  time.sleep(4)
  print(espacio)
  print(Fore.CYAN + Style.BRIGHT + "La gente en la calle me tiraba cosas y los otros gatos me pegaban y me molestaban mucho, y eso me ponía muy triste :(")
  print(gato[1])
  time.sleep(4)
  print(espacio)
  print(Fore.CYAN + Style.BRIGHT + "Es difícil vivir sin nadie que te quiera ¿Sabes? Te hace sentir bastante vacío... Y solo...")
  print(gato[1])
  time.sleep(4)
  print(espacio)
  print(Fore.YELLOW + Style.BRIGHT + "Pero ya no quiero hablar más de eso... ¡Lo importante es que ahora vivo aquí y soy más feliz!")
  print(gato[5])
  time.sleep(4)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "¿Sabes lo feliz que me hace sentir que leas lo que pienso? ¡No puedo ser un gatito más afortunado!")
  print(gato[5])
  time.sleep(4)
  print(espacio)
  print(Fore.YELLOW + Style.BRIGHT + "Tal vez pienses lo contrario, ¡Pero yo creo que eres una muy hermosa persona por disfrutar conocer mi historia de gatito!")
  print(gato[5])
  time.sleep(3)
  print(espacio)
  print(Fore.YELLOW + Style.BRIGHT + "Pocas veces ustedes pueden escucharnos en realidad...")
  print(gato[3])
  time.sleep(3)
  print(espacio)
  print(Fore.YELLOW + Style.BRIGHT + "¡Pero me alegro que ahora sea distinto!")
  print(gato[6])
  time.sleep(3)
  print(espacio)
  print(Fore.GREEN + Style.BRIGHT + f"Y bueno {nombre}... Ya que sabes más sobre mí, ¡Ahora es mi turno de preguntarte a ti! ¿Qué edad tienes?")
  print(gato[5])
  edad = input("")
  if edad <= "25":
    time.sleep(3)
    print(espacio)
    print(Fore.GREEN + Style.BRIGHT + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida")
    print(gato[5])
    time.sleep(3)
    print(espacio)
    print(Fore.GREEN + Style.BRIGHT + f"¿O no?")
    print(gato[4])
    time.sleep(3)
    print(espacio)
    print(Fore.WHITE + Style.BRIGHT + f"Bueno, aunque eso igual no me concierne mucho, pero... ¡Pensaré que eres una persona muy feliz igualmente!")
    print(gato[4])
    time.sleep(3)
    print(espacio)
    print(Fore.MAGENTA + Style.BRIGHT + f"Digo, ¿Cómo no puedes estarlo? Yo vivo dentro de esta computadora, ¡Pero tú vives en el mundo real!")
    print(gato[6])
    time.sleep(3)
    print(espacio)
    print(Fore.MAGENTA + Style.BRIGHT + f"Oh {nombre} tienes una libertad increíble, ¡Debes aprovecharla cada instante! ¡No dejes que nadie te la quite jamás!")
    print(gato[5])
    time.sleep(3)
    print(espacio)
    print(Fore.WHITE + Style.BRIGHT + f"Y tampoco dejes la libertad para ser feliz por culpa de nadie, vive tu propia vida {nombre} ¡COMO YO!")
    print(gato[5])
    time.sleep(3)
  elif edad > "25":
    time.sleep(3)
    print(espacio)
    print(Fore.GREEN + Style.BRIGHT + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!")
    print(gato[5])
    time.sleep(4)
    print(espacio)
    print(Fore.YELLOW + Style.BRIGHT + f"¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!")
    print(gato[6])
elif pregunta1 == "2":
  time.sleep(1)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "¿Sabes que dicen que la curiosidad mató al gato no?")
  print(gato[4])
  time.sleep(3)
  print(espacio)
  print(Fore.RED + Style.BRIGHT + "Es una frase muy cruel que dicen ustedes")
  print(gato[0])
  time.sleep(3)
  print(espacio)
  print(Fore.RED + Style.BRIGHT + "¡A mí no me ha matado ninguna curiosidad! ¿Por qué dicen eso?")
  print(gato[0])
  time.sleep(3)
  print(espacio)
  print(Fore.CYAN + Style.BRIGHT + "Pero admito que soy muy curioso...")
  print(gato[9])
  time.sleep(3)
  print(espacio)
  print(Fore.GREEN + Style.BRIGHT + "¡Pero bueno! Ya sé tu nombre, ehm... ¿Qué edad tienes?\n")
  print(gato[4])
  edad = input("")
  if edad <= "25":
    time.sleep(3)
    print(espacio)
    print(Fore.GREEN + Style.BRIGHT + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida")
    print(gato[5])
    time.sleep(3)
  elif edad > "25":
    time.sleep(3)
    print(espacio)
    print(Fore.GREEN + Style.BRIGHT + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!")
    print(gato[5])
    time.sleep(4)
    print(espacio)
    print(Fore.YELLOW + Style.BRIGHT + f"¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!")
    print(gato[6])
    time.sleep(4)
print(espacio)
print(Fore.GREEN + Style.BRIGHT + f"Sabes... ¡Me caes demasiado bien {nombre}!")
print(gato[4])
time.sleep(3)
print(espacio)
print(Fore.YELLOW + Style.BRIGHT + f"Sé que es algo precipitado pero... ¿Te gustaría ser mi dueño?")
print(gato[7])
time.sleep(2)
pregunta2 = input(Fore.GREEN + Style.BRIGHT + """
                                          Responde.
                            [¡Claro que si!]      -      [No.]
                                   (1)                    (2) \n""")
if pregunta2 == "1":
  time.sleep(3)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "¡¡¿¡EN SERIOOOO?!!? NO SÉ QUE DECIR ESTOY DEMASIADO FELIZ OMG")
  print(gato[7])
  time.sleep(3)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "TE")
  print(gato[7])
  time.sleep(1)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "AMO")
  print(gato[7])
  time.sleep(1)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "DEMASIADO")
  print(gato[8])
  time.sleep(1)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  print(gato[8])
  time.sleep(1)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "Perdona el ataque de emoción, ya me calmo...")
  print(gato[6])
  time.sleep(3)
  print(espacio)
  print(Fore.YELLOW + Style.BRIGHT + "Es que, ¡Al fin tengo un dueño! ¡Es la primera vez que tengo uno!")
  print(gato[7])
  time.sleep(3)
  print(espacio)
  print(Fore.YELLOW + Style.BRIGHT + "Bien ehm... ¿Qué sigue? ¡OH SI YA SÉ!")
  print(gato[4])
  time.sleep(3)
  print(espacio)
  print(Fore.MAGENTA + Style.BRIGHT + "¿Qué nombre te gustaría ponerme? \n")
  print(gato[4])
  namecat = input("")
  namecatmayus = namecat.upper()
  time.sleep(2)
  print(espacio)
  print(Fore.YELLOW + Style.BRIGHT + f"OH {namecatmayus} ¡QUE LINDO NOMBRE GRACIAS {nombremayus}!")
  print(gato[4])
  time.sleep(3)
#continuar
if pregunta2 == "2":
  time.sleep(2)
  print(espacio)
  print(Fore.RED + Style.BRIGHT + f"¡¿¡CÓMO QUE NO!? QUÉ HE HECHO MAL PARA QUE NO QUIERAS ADOPTARME {nombremayus}!")
  print(gato[0])
  time.sleep(3)
  print(espacio)
  print(Fore.RED + Style.BRIGHT + f"¿ACASO ME ODIAS {nombremayus}?")
  print(gato[0])
  time.sleep(3)
  pregunta3 = input(Fore.GREEN + Style.BRIGHT + """
                                          Responde.
                            [¡Claro que si!]      -      [No.]
                                   (1)                    (2) \n""")
  if pregunta3 == "1":
    time.sleep(1)
    print(Fore.RED + Style.BRIGHT + "¿QUÉ?")
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + "¡NO!")
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + "TU")
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + "MIENTES")
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + "ERES")
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + "UNA")
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + "MALA")
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + "PERSONA")
    time.sleep(2)
    print(espacio)
    print(Fore.RED + Style.BRIGHT + ".")
    time.sleep(1)
    print(espacio)
    print(Fore.RED + Style.BRIGHT + "..")
    time.sleep(1)
    print(espacio)
    print(Fore.RED + Style.BRIGHT + "...")
    time.sleep(3)
