cantidad = 0
i = 0
ciudades = []   

cantidad = int(input("Ingrese la cantidad de ciudades que desea agregar: "))

if cantidad > 0:
    while i < cantidad:
        ciudad = input("Ingrese el nombre de la ciudad: ")
        ciudades.append(ciudad)
        i += 1  
    print("Las ciudades ingresadas son:")
    for ciudad in ciudades:
        print(ciudad)       
else:
    print("La cantidad debe ser mayor a 0.")