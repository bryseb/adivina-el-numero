#                                     ADIVINA EL NUMERO
               # iportamos creador de random numeros


import time              # para q se demore un poco entre lineas al final
import random            # para poner numeros aleatorios
import os                # para limpiar la pantalla


                 # creamos el loop del juego para todo el juego
while True:

    intento = 0
    Num_user = None
    Num_x_Adivinar = random.randint(1, 100)

                #funcion def, hacemos una introduccion al juego!!!

    def intro():    
        print("*"*100)
        print(" "*25 ,"ADIVINA EL NUMERO Q ESTOY PENSANDO DEL 1 al 100")
        print("*"*100, )
        print("                   Tienes 8 INTENTOS !!   bueno...bueno..10 intentos YA!?\n ")
    
                   # llamamos a al funtion intro
    intro()             


                    # loop de q si es menos a 9 puede jugar hasta  q adivine o se cumplen ,los 10

    while intento <= 9:
        intento = intento + 1
        Num_user = (input("Intento #" + str(intento) + ": "))   # para q salga el intento # cada q el user lo haga      
        if Num_user.isdigit():                                 # con este isdigit comprobamos q lo q pone el user sea solo numeros
            Num_user = int(Num_user)                           # y le decimos q si lo es lo ponga como numero inter
            if Num_user > Num_x_Adivinar:
                print("          es menor" )
            elif Num_user < Num_x_Adivinar:
                print("          es mayor")
            else:
                print("\n     HHHUAAUU!  NO MANCHES!!!  ADIVINASTE.  En", intento, "Intentos")
                break
        else:
            print("      q pasooo!!! SOLO numeros enteros")

    if Num_user != Num_x_Adivinar:                                    #salimos de el loop de los intentos porq ya conto los 10 y no adivino 
        print("\n     perdiste el numero era el :",Num_x_Adivinar ) 

    time.sleep(1)                                                     # le damos 1 seg para q aparesca la siguiente linea

    input("\n aplasta una teclita........")

    os.system ("clr")                                                   #limpia la pantalla en 2 seg
    time.sleep(2)        

    Continuar = (input("\n   Jugamos otrita ??     me tomo 3 meses aprender esto!!  plsss s/n:  "))     # fuera del loop le ponemos la pregunta de continuar o no
    if (Continuar != "s"):
        break

    os.system ("clr")                                               # limpia la pantalla en 1 seg
    time.sleep(1)
