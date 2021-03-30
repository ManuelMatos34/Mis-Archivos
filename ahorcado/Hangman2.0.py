#HANGMAN
#Manuel Matos
#19-1597

import random
import os

palabras=["AZUCAR", 'CHOCOLATE', 'COCODRILO', 'CASA', 'PERRO']
palabra = (random.choice(palabras))

letrasCorrectas= ""
todaslasLetras= ""
intentos= 0    

intento0= """ 

      o===o
      |   |
          |
          |
          |
          |
    =========
        """
intento1= """ 

      o===o
      |   |
     [0]  |
          |
          |
          |
    =========
        """

   
intento2=  """
      o===o
      |   |
     [0]  |
    --|-- |
    _/|_  |
          |
    =========
        """


while True:

    os.system("cls")

    print("==================")
    print('****BIENVENIDO****')
    print('*****AL JUEGO*****')
    print('*****HANGMAN*****')
    print("==================")

    if intentos == 0:
       print (intento0)
    elif intentos == 1:
       print (intento1)
    elif intentos == 2:
        print(intento2)

    print()

    respuesta = ""
    

    for L in palabra:
         if L in letrasCorrectas:
            respuesta += L
         else:
            respuesta += "_"   

    print("         {}".format(respuesta))

    print()
    print()

    if respuesta == palabra:
        print("===HAS GANADO===")
        print("===FELICIDADES===")
        print("===TE SALVASTE===")
        print()

    if intentos > 2:
        print("LA PALABRA CORRECTA ES:", palabra)
        print('===HAS PERDIDO===')
        print('===HAS MUERTO====')
        print()


    while True:
        letraMinuscula=input('DAME UNA LETRA PORFAVOR: ')
        letraOficial= letraMinuscula.upper()
        if len(letraOficial) < 1 or len(letraOficial)>1:
            print('INTRODUCE UNA LETRA')
        elif letraOficial in todaslasLetras:
            print('ESA LETRA YA LA HAS PUESTO')
        elif not letraOficial.isalpha():
            print("INTRODUCE UNA LETRA")
        else:
            todaslasLetras += letraOficial
            break

    if letraOficial not in palabra:
        intentos +=1
    else:
        letrasCorrectas += letraOficial
