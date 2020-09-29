def negocio():
    cliente = input("Ingrese el nombre: ")
    producto = input("Ingrese el producto: ")
    precio = float(input("precio del producto: "))
    concluir = input("¿Concluirás algo?")

    while concluir == "false":
        cliente = cliente + "," + input("Ingrese el nombre: ")
        producto = producto + "," + input("Ingrese el producto: ")
        precio = precio + float(input("precio del producto. "))
        concluir = input("¿Concluirás algo?")

    if concluir == "true":
        print("Historial del dia: ")
        print("cliente1.", cliente)
        print("productos:", producto)
        print("Total: ", precio)
    else:
        print("ERROR, no se han completados todos los campos.")

negocio()
