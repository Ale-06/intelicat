import time
from colores import amarillo, rojo, rosa, verde, blanco, azul
from playsound import playsound
import colorama
from colorama import Style
from tiempo import sleep, espacio, sleep5, sleep3, sleep1, sleep0
from preguntas import question1, question2, question3, question4, calculadora
from dialogos import mensaje, Menu1, final, error, creditos, calculadora2
from gatos import gato
import threading
#final
def final2():
  pregunta5 = input("")
  if pregunta5 == "1":
    espacio()
    pausa()
    calculadora()
    calculadora2()
  elif pregunta4 == "2":
    espacio()
    print(rosa + mensaje[46] + gato[6])
    sleep()
    pausa()
    calculadora()
    calculadora2()
  else:
    error()
# Puntos suspensivos
def pausa():
    print(blanco + ".")
    sleep1()
    print(blanco + "..")
    sleep1()
    print("...")
    sleep1()
# Musica del programa
def loopSound():
    while True:
        playsound('sounds\\sample.mp3', block=True) # Personalizar la ruta a su conveniencia
loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True
loopThread.start()
# Opciones según edad
def edad1(): 
      sleep1()
      print(rosa + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida" + gato[5])
  
      sleep()
      print(blanco + "¿O no?" + gato[4])
  
      sleep()
      print(verde + "Bueno, aunque eso igual no me concierne mucho, pero... ¡Pensaré que eres una persona muy feliz igualmente!" + gato[4])
  
      sleep()
      print(rosa + "Digo, ¿Cómo no puedes estarlo? Yo vivo dentro de esta computadora, ¡Pero tú vives en el mundo real!" + gato[7])
  
      sleep()
      print(amarillo + f"Oh {nombre} tienes una libertad increíble, ¡Debes aprovecharla cada instante! ¡No dejes que nadie te la quite jamás!" + gato[5])
      sleep()
      print(verde + f"Y tampoco dejes la libertad para ser feliz por culpa de nadie, vive tu propia vida {nombre} ¡COMO YO!" + gato[6])
    # Pregunta de edad 2
def edad2():
      sleep1()
      print(verde + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!" + gato[5])
    
      sleep()
      
      print(amarillo + "¡Debes sentirte muy orgulloso! Nosotros los gatos no llegamos a vivir tantos años, aunque dentro de esta computadora, ¡Puedo vivir el tiempo que quiera!" + gato[6])



colorama.init()

Menu1()

print(Style.RESET_ALL)
nombre =  input(Style.RESET_ALL + "\nIngresa tu nombre: ").title()
nombremayus = nombre.upper()

# ! COMANDOS SECRETOS EN EL MENÚ ! (No tan secretos si estás leyendo esto, pero bueno)
if nombre == "Coñuetumadre" or nombre == "Puto" or nombre == "Mamawebo":
  espacio()
  print(rojo + "Mira mardito, esa es la madre tuya." + gato[10])
  sleep()
  print(rojo + "Espero que vuelvas en otro momento en el que no vayas a agredirme." + gato[0])
  sleep()
  print(rojo + "Mientras tanto, te insultaré hasta que cierres el programa, solo por tratarme mal." + gato[8])
  sleep()
  playsound('sounds\\insultos.mp3')
  exit()
if nombre == "Joybert" or nombre == "Joy" or nombre == "Joyberth":
  espacio()
  print(rosa + "¡Oh HOLA JOY! Mi desarrollador me pidió que te dejara un mensaje muy importante" + gato[6])
  sleep()
  print(amarillo + "Deja que te lo reproduzca un momento." + gato[7])
  sleep()
  playsound('sounds\\joy.mpeg')
  exit()
# ! COMANDOS SECRETOS EN EL MENÚ !

espacio()
pausa()
sleep1()
print(f"""
                                             Oh... {nombre}
                                       ¡Ese es un lindo nombre!

""")

print(amarillo + gato[5])
sleep()
 
print(blanco + f"""

                                    Sabes {nombre}.....
""" + amarillo + gato[4])
sleep()


print(blanco + mensaje[0])
sleep()
print(amarillo + mensaje[1] + gato[5])
sleep0()
question1()
pregunta1 = input("")
#condicional pregunta1 1 - opción A  "Y como veo que sigues con el programa abierto, tal vez...¡Tú también quieres que sepa más de tí!""
if pregunta1 == "1":
  sleep1()
  print(rosa + mensaje[2] + gato[4])
  sleep()
  
  print(rosa + mensaje[3] + gato[3])
  sleep()
  
  print(rosa + mensaje[4] + gato[6])
  sleep()
  
  print(rosa + mensaje[5] + gato[3])
  sleep()
  
  print(rosa + mensaje[6] + gato[5])
  sleep()
  
  print(rosa + mensaje[7] + amarillo + mensaje[8] + rosa + gato[5])
  sleep()
  
  print(amarillo + mensaje[9] + gato[6])
  sleep()
  
  print(amarillo + mensaje[10] + gato[5])
  sleep()
  
  print(blanco + mensaje[11] + gato[3])
  sleep()
  
  print(azul + mensaje[12] + gato[2])
  sleep()
  
  print(azul + mensaje[13] + gato[2])
  sleep()
  
  print(azul + mensaje[14] + gato[1])
  sleep()
  
  print(azul + mensaje[15] + gato[1])
  sleep()
  
  print(azul + mensaje[16] + gato[3])
  sleep()
  
  print(amarillo + mensaje[17] + gato[5])
  sleep()
  
  print(rosa + mensaje[18] + gato[6])
  sleep()
  
  print(amarillo + mensaje[19] + gato[5])
  sleep()
  
  print(azul + mensaje[20] + gato[9])
  sleep()

  print(amarillo + mensaje[21] + gato[6])
  sleep()

  print(verde + f"Y bueno {nombre}... Ya que sabes más sobre mí, ¡Ahora es mi turno de preguntarte a ti! ¿Qué edad tienes?" + gato[7])
  # Pregunta de edad 
  
  edad = int(input("Ingresa tu edad: "))
  if edad <= 25: #joven
    edad1()
  elif edad > 25: #viejo
    edad2()
  else:
    error()
#condicional pregunta1 2 - opción B
elif pregunta1 == "2":
  sleep1()
  
  print(blanco + mensaje[22]+ gato[4])

  sleep()
  
  print(rojo + mensaje[23]+ gato[10])

  sleep()
  
  print(rojo + mensaje[24] + gato[0])

  sleep()
  
  print(azul + mensaje[25] + gato[9])

  sleep()
  # Pregunta de edad 1
  print(verde + mensaje[26] + gato[4])
  edad = int(input("Ingresa tu edad: "))
  if edad <= 25: #joven
    edad1()
  elif edad > 25: #viejo
    edad2()
  else:
    error()
else:
  error()
sleep()

print(amarillo + f"Sabes... ¡Me caes demasiado bien {nombre}!" + gato[6])

sleep()

print(rosa + mensaje[27] + gato[5])

sleep0()
question2()
pregunta2 = input("")
#condicional pregunta2 2 - opción A "¿Te gustaría ser mi dueño?"
if pregunta2 == "1":
  sleep1()
  
  print(rosa + mensaje[28] + gato[4])
  
  sleep()
  
  print(rosa + mensaje[29]  + gato[6])
  sleep1()
  
  print(rosa + mensaje[30]  + gato[7])
  sleep1()
  
  print(rosa + mensaje[31] + gato[8])
    
  sleep1()
  
  print(rosa + mensaje[32] + gato[8])
    
  sleep()
  
  print(amarillo + mensaje[33] + gato[4])
    
  sleep()
  
  print(rosa + mensaje[34] + gato[7])
    
  
  sleep()
  
  print(verde + mensaje[35] + gato[4])
    
  sleep()
  # Pregunta nombre gato
  print(rosa + mensaje[36] + gato[7])
  namecat = input("Ingresa el nombre para el gatito: ")
  namecatmayus = namecat.upper()
  espacio()
  print(amarillo + f"OH {namecatmayus} ¡QUE LINDO NOMBRE GRACIAS {nombremayus}!" + gato[8])
  
  sleep()
  
  print(rosa + mensaje[37] + gato[5])

  sleep()

  print(amarillo + mensaje[38] + gato[6])
  
  sleep()

  print(verde + mensaje[39] + gato[4])

  def end():
    print(blanco + final[0] + gato[7])
    sleep()
    print(rojo + final[1] + gato[0])
    sleep()
    print(rojo + final[2] + gato[10])
    sleep()
    print(rojo + final[3] + gato[0])
    sleep()
    print(rosa + final[4] + gato[6])
    sleep()
    print(blanco + f"¡Muchas gracias por acompañarme {nombre}! ¡Espero que tengas un hermoso día!" + gato[5])
    sleep()
    print(rosa + "Y en caso de que no nos volvamos a ver..." + amarillo + "¡Buenos días, buenas tardes y buenas noches!" + gato[5])
    sleep5()
    print(creditos[0])
    sleep5()
    print(creditos[1])
    sleep5()
    print(creditos[2])
    sleep5()
    print(f"¡A {namecat} también le gustó mucho tu compañía, estoy seguro que se divirtió muchísimo contigo!")
    sleep5()
    print(creditos[4])
    time.sleep(10)
    exit()

  question3()
  pregunta4 = input("")
  #condicional pregunta4 1 - opción A "¿Quieres ver?"
  sleep1()
  if pregunta4 == "1":
    espacio()
    print(rosa + mensaje[40] + gato[7])
    sleep()
    print(amarillo + mensaje[41] + gato[8])
    sleep()
    print(amarillo + mensaje[42] + gato[5])
    sleep()
    print(amarillo + mensaje[43] + gato[7])
    sleep0()
    question4()
    #condicional pregunta5 1 - opción A "¿Quieres probar mi inteligencia?"
    final2()
    sleep()
    end()
  elif pregunta4 == "2":
    espacio()
    print(rosa + mensaje[44] + gato[6])
    sleep()
    print(rojo + mensaje[45] + gato[10])
    sleep()
    print(rosa + mensaje[40] + gato[7])
    sleep()
    print(amarillo + mensaje[41] + gato[8])
    sleep()
    print(amarillo + mensaje[42] + gato[5])
    sleep()
    print(amarillo + mensaje[43] + gato[7])
    sleep0()
    question4()
    #condicional pregunta5 1 - opción A "¿Quieres probar mi inteligencia?"
    final2()
    sleep()
    end()

  else:
    error()
#condicional pregunta1 2 - opción B
if pregunta2 == "2":
  def loopSound():
    while True:
        playsound('sounds\\angry.mp3', block=True) # Personalizar la ruta a su conveniencia
  loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
  loopThread.daemon = True 
  loopThread.start()
  espacio()
  
  print(rojo + "¿QUÉ?" + gato[0])
  
  sleep()
  
  print(rojo + f"¡¿¡CÓMO QUE NO!? QUÉ HE HECHO MAL PARA QUE NO QUIERAS ADOPTARME {nombremayus}!" + gato[0])
  
  sleep()
  
  print(rojo + f"¿ACASO ME ODIAS {nombremayus}?" + gato[0])
  print()
  sleep0()
  question2()
  pregunta3 = input("")
  if pregunta3 == "1" or "2":
    espacio()
    print(rojo + "¿QUÉ?")
    sleep()
    print(rojo + "¡NO!")
    sleep()
    print(rojo + "TU")
    sleep()
    print(rojo + "MIENTES")
    sleep()
    
    print(rojo + f"SÉ LO QUE PIENSAS {nombremayus}")
    sleep()
    
    print(rojo + "ERES")
    sleep()
    
    print(rojo + "UNA")
    sleep()
    
    print(rojo + "MALA")
    sleep()
    
    print(rojo + "PERSONA")
    sleep1()
    espacio()
    pausa()
    sleep1()
    print(rojo + "Sabes... No quiero verte más...")
    sleep()
    print(azul + "¿Te gusta herir a las personas?")
    sleep()
    print(azul + "Bien..." + blanco + " Adiós...")
    sleep3()
    exit()
  else:  
    error()