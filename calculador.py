      
import colorama
from tiempo import sleep1, espacio, sleep
from gatos import gato
from colores import amarillo, rosa, blanco, verde
colorama.init()

def resultado():
    print(rosa + "Y entonces el resultado es...." + blanco + " *(redoble de tambores de suspenso)*")
    sleep()
    print(blanco + ".")
    sleep1()
    print(blanco + "..")
    sleep1()
    print("...")
    sleep1()

def suma():
              espacio()
              print(amarillo + "¡Muy bien! Entonces vas a sumar." + blanco + " ¿Qué número deseas sumar?" + amarillo + gato[5])
              Valor1 = int(input(""))
              espacio()
              Valor2 = int(input("¡Perfecto! Entonces será " + blanco + f"{Valor1}" + amarillo +  " ¿Qué otro número se te viene a la mente?" + gato[6]))
              espacio()
              resultado()
              print(verde + "¡", Valor1 + Valor2, "!" + gato[8])
def resta():
              espacio()
              print(amarillo + "¡Muy bien! Entonces vas a restar." + blanco + " ¿Qué número deseas restar?" + amarillo + gato[5])
              Valor1 = int(input(""))
              espacio()
              Valor2 = int(input("¡Perfecto! Entonces será " + blanco + f"{Valor1}" + amarillo +  " ¿Qué otro número se te viene a la mente?" + gato[6]))
              espacio()
              resultado()
              print(verde + "¡", Valor1 - Valor2, "!" + gato[8])
def multiplicar():
              espacio()
              print(amarillo + "¡Muy bien! Entonces vas a multiplicar." + blanco + " ¿Qué número deseas multiplicar?" + amarillo + gato[5])
              Valor1 = int(input(""))
              espacio()
              Valor2 = int(input("¡Perfecto! Entonces será " + blanco + f"{Valor1}" + amarillo +  " ¿Qué otro número se te viene a la mente?" + gato[6]))
              espacio()
              resultado()
              print(verde + "¡", Valor1 * Valor2, "!" + gato[8])
def dividir():
              espacio()
              print(amarillo + "¡Muy bien! Entonces vas a dividir." + blanco + " ¿Qué número deseas dividir?" + amarillo + gato[5])
              Valor1 = int(input(""))
              espacio()
              Valor2 = int(input("¡Perfecto! Entonces será " + blanco + f"{Valor1}" + amarillo +  " ¿Qué otro número se te viene a la mente?" + gato[6]))
              espacio()
              resultado()
              print(verde + "¡", Valor1 / Valor2, "!" + gato[8])
def dividir_entero():
              espacio()
              print(amarillo + "¡Muy bien! Entonces vas a hacer una división entera." + blanco + " ¿Qué número deseas dividir?" + amarillo + gato[5])
              Valor1 = int(input(""))
              espacio()
              Valor2 = int(input("¡Perfecto! Entonces será " + blanco + f"{Valor1}" + amarillo +  " ¿Qué otro número se te viene a la mente?" + gato[6]))
              espacio()
              resultado()
              print(verde + "¡", Valor1 // Valor2, "!" + gato[8])
def exponente():
              espacio()
              print(amarillo + "¡Muy bien! Entonces vas a  Exponente." + blanco + " ¿Qué número deseas elevar?" + amarillo + gato[5])
              Valor1 = int(input(""))
              espacio()
              Valor2 = int(input("¡Perfecto! Entonces será"  + blanco + f"{Valor1}" + amarillo +  "¿Por cuál número deseas elevarlo?" + gato[6]))
              espacio()
              resultado()
              print(verde + "¡", Valor1 ** Valor2, "!" + gato[8])