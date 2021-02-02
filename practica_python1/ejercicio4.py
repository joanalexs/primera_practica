mes=int(input("Ingrese el numero del mes:"))
if mes>=1 and mes<=3:
    print("Se encuentra en el primer trimestre")
elif mes>=4 and mes<=6:
    print("Se encuentra en el segundo trimestre")
elif mes>=7 and mes<=9:
    print("Se encuentra en el tercer trimestre") 
elif mes>=10  and mes<=12:
    print("Se encuentra en el cuarto  trimestre")
else:
    print("Error,los meses del año no pueden ser mayor a 12 ")