import time
from colores import amarillo, rojo, rosa, verde, blanco, azul
from playsound import playsound
import colorama
from colorama import Fore, Style
from tiempo import sleep1, sleep2, sleep3, sleep4, sleep10, espacio, sleep5
from preguntas import question1, question2, question3, question4, calculadora
from dialogos import mensaje, final, error, creditos
from gatos import gato, alternativo
from calculador import suma, resta, multiplicar, dividir, dividir_entero, exponente
import threading
def loopSound():
    while True:
        playsound('C:\\Users\\Juan Rondon\\Desktop\\Codigo, paginas y proyectos\\python\\intelicat\\sounds\\sample.mp3', block=True) # Personalizar la ruta a su conveniencia

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

espacio()
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

i = len(mensaje)
for i in range(len(mensaje)):
  print(mensaje[40])
  sleep3()
  print(amarillo + mensaje[1] + gato[5])
  sleep10()
  question1()
  pregunta1 = input("")
  if pregunta1 == "1":
    sleep1()
    print(rosa + mensaje[2] + gato[4])
  #  print(gato[4])
    sleep2()
    
    print(rosa + mensaje[3] + gato[3])
    sleep2()
    
    print(rosa + mensaje[4] + gato[6])
    sleep2()
    
    print(rosa + mensaje[5] + gato[3])
    sleep3()
    
    print(rosa + mensaje[6] + gato[5])
    sleep3()
    
    print(rosa +mensaje[7] + amarillo + mensaje[8] + rosa + gato[5])
    sleep3()
    
    print(mensaje[9] + gato[5])
    sleep3()
    
    print(mensaje[10] + gato[5])
    sleep3()
    
    print(blanco + mensaje[11] + gato[3])
    sleep3()
    
    print(azul + mensaje[12] + gato[2])
    sleep4()
    
    print(azul + mensaje[13] + gato[2])
    sleep3()
    
    print(azul + mensaje[14] + gato[1])
    sleep4()
    
    print(azul + mensaje[15] + gato[1])
    sleep4()
    
    print(azul + mensaje[16] + gato[1])
    sleep4()
    
    print(amarillo + mensaje[17] + gato[5])
    sleep4()
    
    print(rosa + mensaje[18] + gato[5])
    sleep4()
    
    print(amarillo + mensaje[19] + gato[5])
    sleep3()
    
    print(amarillo + mensaje[20] + gato[3])
    sleep3()
    
    print(amarillo + mensaje[21] + gato[6])
    sleep3()
    
    print(verde + f"Y bueno {nombre}... Ya que sabes más sobre mí, ¡Ahora es mi turno de preguntarte a ti! ¿Qué edad tienes?" + gato[5])
    edad = input("")
    if edad <= "25":
      sleep3()
      print(verde + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida" + gato[5])
  
      sleep3()
      print(verde + mensaje[22] + gato[4])
  
      sleep4()
      print(blanco + mensaje[23] + gato[4])
  
      sleep4()
      print(rosa + mensaje[24] + gato[6])
  
      sleep3()
      print(rosa + f"Oh {nombre} tienes una libertad increíble, ¡Debes aprovecharla cada instante! ¡No dejes que nadie te la quite jamás!" + gato[5])
  
      sleep3()
      print(blanco + f"Y tampoco dejes la libertad para ser feliz por culpa de nadie, vive tu propia vida {nombre} ¡COMO YO!" + gato[5])
      sleep3()
    elif edad > "25":
      sleep3()
      print(verde + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!" + gato[5])
    
      sleep4()
      
      print(amarillo + mensaje[25] + gato[6])
    
  elif pregunta1 == "2":
    sleep1()
    
    print(rosa + mensaje[26]+ gato[4])
  
    sleep3()
    
    print(rojo + mensaje[27] + gato[0])
  
    sleep3()
    
    print(rojo + mensaje[28] + gato[0])
  
    sleep3()
    
    print(azul + mensaje[29] + gato[9])
  
    sleep3()
    
    print(verde + mensaje[30] + gato[4])
  
    edad = input("")
    if edad <= "25":
      sleep3()
      
      print(verde + f"Oh {edad}... ¡Eres una persona muy jóven! Me imagino que disfrutas mucho tu vida" + gato[5])
      
      sleep3()
    elif edad > "25":
      sleep3()
      
      print(verde + f"Oh {edad}... Eres algo viejo... ¡Pero eso no está mal claro!" + gato[5])
      
      sleep4()
      
      print(amarillo + mensaje[31] + gato[6])
      
      sleep4()
  else:
    error()
  
  print(verde + f"Sabes... ¡Me caes demasiado bien {nombre}!" + gato[4])
  
  sleep3()
  
  print(amarillo + mensaje[32] + gato[7])
  
  sleep10()
  question2()
  pregunta2 = input("")
  if pregunta2 == "1":
    sleep3()
    
    print(rosa + mensaje[33] + gato[7])
    
    sleep3()
    
    print(rosa + mensaje[34]  + gato[7])
    sleep3()
    
    print(rosa + mensaje[35]  + gato[7])
    sleep3()
    
    print(rosa + mensaje[36] + gato[8])
      
    sleep3()
    
    print(rosa + mensaje[37] + gato[8])
      
    sleep3()
    
    print(rosa + mensaje[38] + gato[6])
      
    sleep3()
    
    print(amarillo + mensaje[39] + gato[7])
      
    sleep3()
    
    print(amarillo + mensaje[40] + gato[4])
      
    sleep3()
    
    print(rosa + mensaje[41] + gato[4])
      
    namecat = input("")
    namecatmayus = namecat.upper()
    sleep2()
    
    print(amarillo + f"OH {namecatmayus} ¡QUE LINDO NOMBRE GRACIAS {nombremayus}!" + gato[4])
      
    sleep3()
    
    print(rosa + mensaje[42] + gato[8])
      
    sleep3()
    
    print(rosa + mensaje[43] + gato[7])

    sleep3()
    
    print(rosa + mensaje[44] + gato[6])
    question3()
    pregunta4 = input("")
    if pregunta4 == "1":
      sleep1()
      print(amarillo + mensaje[45] + gato[5])
      sleep3()
      print(verde + mensaje[46] + gato[4])
      sleep3()
      print(rosa + mensaje[47] + gato[8])
      sleep4()
      print(amarillo + mensaje[48] + gato[4])
      sleep10()
      question4()
      pregunta5 = input("")
      if pregunta5 == "1":
        calculadora()
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
      elif pregunta4 == "2":
        print()
      else:
        error()
      sleep3()
      print(blanco + final[0] + gato[6])
      sleep3()
      print(rojo + final[1] + gato[0])
      sleep3()
      print(rojo + final[2] + gato[10])
      sleep3()
      print(rojo + final[3] + gato[0])
      sleep3()
      print(rosa + final[4] + gato[5])
      sleep3()
      print(blanco + f"¡Muchas gracias por acompañarme {nombre}! ¡Espero que tengas un hermoso día!" + gato[6])
      sleep3()
      print(rosa + "Y en caso de que no nos volvamos a ver..." + amarillo + "¡Buenos días, buenas tardes y buenas noches!" + gato[5])
      sleep5()
      print(creditos[0])
      sleep5()
      print(creditos[1])
      sleep5()
      print(creditos[2])
      sleep5()
      print(creditos[3])
      sleep5()
      print(creditos[4])
      time.sleep(10)
    elif pregunta4 == "2":
      print()
    else:
      error()
  if pregunta2 == "2":
    def loopSound():
      while True:
          playsound('C:\\Users\\Juan Rondon\\Desktop\\Codigo, paginas y proyectos\\python\\intelicat\\sounds\\angry.mp3', block=True) # Personalizar la ruta a su conveniencia
    loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
    loopThread.daemon = True 
    loopThread.start()
    sleep1()
    
    print(rojo + "¿QUÉ?" + gato[0])
    
    sleep2()
    
    print(rojo + f"¡¿¡CÓMO QUE NO!? QUÉ HE HECHO MAL PARA QUE NO QUIERAS ADOPTARME {nombremayus}!" + gato[0])
    
    sleep3()
    
    print(rojo + f"¿ACASO ME ODIAS {nombremayus}?" + gato[0])
    print()
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
      error()