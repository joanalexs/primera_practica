msj="""
Ingrese una opcion por favor:
cuadrado=1
rectangulo=2
"""
print(msj)
opcion=int(input("Ingrese la opcion elegida:"))

if opcion==1:
    longitud=int(input("Ingrese la longitud:"))
    ancho=int(input("Ingrese el ancho:"))
    area=(longitud*ancho)**2
    print(f"El area del cuadrado es:{area}")
elif opcion==2:
    longitud=int(input("Ingrese la longitud:"))
    ancho=int(input("Ingrese el ancho:"))
    per=(ancho+longitud)*2
    print(f"El perimetro del rectangulo es:{per}")
else:
    print("Error,eliga una opcion correcta por favor")