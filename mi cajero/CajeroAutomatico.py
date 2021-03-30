#Cajero Automatico
#Manuel Matos
#19-1597

print()
print('==================================')
print('==================================')
print('======BIENVENIDO A CITY BANK======')
print("==================================")
print('==================================')
print()
saldocliente=int(200000)
intentospin=1
while intentospin<=3:

    PIN = int(input("Ingrese su PIN:"))
    print("")
    if PIN==12345:
        
        intentospin=4
        print()
        clientes= open('cliente1.txt', "r")
        cliente= (clientes.read())
        print(cliente)
        print()
        print("   .:::<>OPCIONES<>:::.")
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Ver el saldo disponible")
        print("4. Salir")
        opcion = int(input("Eliga una Opcion: "))

        
        if opcion==1:
            print("Digame la cantidad que desea ingresar: ")
            ingreso=int(input())
            desarrollo= saldocliente+ingreso
            print("AHORA SU BALANCE ES DE: ", desarrollo )

        if opcion==2:
            print("Digame la cantidad que desea retirar: ")
            retiro=int(input())
            desarrollo1= saldocliente-retiro
            print("AHORA SU BALANCE ES DE: ", desarrollo1 )

        if opcion==3:
            print('Su saldo es de', saldocliente)
            print()

        if opcion==4:
            print("HA SALIDO SATISFACTORIAMENTE")

   
    else:
        print("EL PIN INGRESADO NO ESTA EN NUESTRA BASE DE DATOS")
        print()
        print()   
        if intentospin==3:
            print("===HA LLEGADO AL LIMITE DE INTENTOS===")
            print("LO SENTIMOS SU CUENTA HA SIDO BLOQUEADA")
            print("====VOLVER A INTENTARLO MAS TARDE====")     
            print()
            print()
        intentospin=intentospin+1


input("")