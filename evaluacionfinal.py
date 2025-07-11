productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD', [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    total = 0
    marca = marca.lower()
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            total += stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {total}")

def búsqueda_ram_precio(ram_min, ram_max, precio):
    encontrados = False
    for modelo, datos in productos.items():
        try:
            ram = int(datos[2].replace("GB", ""))
        except:
            continue
        if ram_min <= ram <= ram_max and modelo in stock and stock[modelo][1] > 0 and stock[modelo][0] <= precio:
            print(datos)
            encontrados = True
    if not encontrados:
        print("No hay notebooks que mostrar.")

def eliminar_producto(modelo):
    if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock[modelo]
        return True
    else:
        return False

def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Eliminar producto.")
        print("4. Salir.")
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        if opcion == "2":
            while True:
                try:
                    ram_min = int(input("Ingrese RAM mínima: "))
                    ram_max = int(input("Ingrese RAM máxima: "))
                    precio = int(input("Ingrese precio: "))
                    búsqueda_ram_precio(ram_min, ram_max, precio)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

        if opcion == "3":
            while True:
                modelo = input("Ingrese modelo a eliminar: ")
                if eliminar_producto(modelo):
                    print("Producto eliminado!!")
                else:
                    print("El modelo no existe!!")
                seguir = input("¿Desea eliminar otro producto (s/n)?: ").lower()
                if seguir != "si":
                    break

        if opcion == "4":
            print("Programa finalizado.")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Debe seleccionar una opción válida!!")

menu()
