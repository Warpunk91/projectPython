while True:
    print("Practica de Python")
    print("1. Calculadora basica")
    print("2. Gestion de contactos")
    print("3. Sistema de inventario")
    print("4. Gestion de tareas")
    print("0. Salir")
    print("")
    print("")

    opcionMenuPrincipal = input("Elige una opción: ")
    print("")

    if opcionMenuPrincipal == "0":
        print("Saliendo del programa.")
        break

    if opcionMenuPrincipal == "1":
        def menuCalculadora():
            print("Calculadora Básica")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("0. Salir")
            print("")

        def suma(a, b):
            return a + b

        def resta(a, b):
            return a - b

        def multiplicacion(a, b):
            return a * b

        def division(a, b):
            if b != 0:
                return a / b
            else:
                return "Error: División por cero"


        while True:
            menuCalculadora()
            opcionCalculadora = input("Elige una opción de la calculadora: ")

            if opcionCalculadora == "0":
                print("Saliendo de la calculadora.")
                print("")
                break

            if opcionCalculadora in ["1", "2", "3", "4"]:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcionCalculadora == "1":
                    print(f"Resultado: {suma(num1, num2)}")
                    print("")
                elif opcionCalculadora == "2":
                    print(f"Resultado: {resta(num1, num2)}")
                    print("")
                elif opcionCalculadora == "3":
                    print(f"Resultado: {multiplicacion(num1, num2)}")
                    print("")
                elif opcionCalculadora == "4":
                    print(f"Resultado: {division(num1, num2)}")
                    print("")
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                print("")

    if opcionMenuPrincipal == "2":
        class Contacto:
            def __init__(self, nombre, telefono):
                self.nombre = nombre
                self.telefono = telefono

        def menuContacto():
            print("Gestión de Contactos")
            print("1. Agregar contacto")
            print("2. Mostrar contactos")
            print("3. Buscar contacto")
            print("4. Eliminar contacto")
            print("0. Salir")
            print("")

        contactos = []

        while True:
            menuContacto()
            opcionContactos = input("Elige una opción del gestor de contactos: ")

            if opcionContactos == "0":
                print("Saliendo del Gestor de contactos.")
                print("")
                break

            if opcionContactos == "1":
                nombre = input("Ingresa el nombre: ")
                telefono = input("Ingresa el teléfono: ")
                contacto = Contacto(nombre, telefono)
                contactos.append(contacto)
                print("Contacto agregado.")
                print("")
            elif opcionContactos == "2":
                for c in contactos:
                    print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
                print("")
            elif opcionContactos == "3":
                nombre = input("Ingresa el nombre a buscar: ")
                encontrado = False
                for c in contactos:
                    if c.nombre == nombre:
                        print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
                        print("")
                        encontrado = True
                        break
                if not encontrado:
                    print("Contacto no encontrado.")
                    print("")
            elif opcionContactos == "4":
                nombre = input("Ingresa el nombre del contacto a eliminar: ")
                for c in contactos:
                    if c.nombre == nombre:
                        contactos.remove(c)
                        print("Contacto eliminado.")
                        print("")
                        break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                print("")


    if opcionMenuPrincipal == "3":
        class Producto:
            def __init__(self, nombre, cantidad, precio):
                self.nombre = nombre
                self.cantidad = cantidad
                self.precio = precio

        def menuProductos():
            print("Sistema de Inventario")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Buscar producto")
            print("4. Actualizar cantidad")
            print("5. Eliminar producto")
            print("0. Salir")
            print("")

        inventario = []

        while True:
            menuProductos()
            opcionProductos = input("Elige una opción del sistema de inventario: ")

            if opcionProductos == "0":
                print("Saliendo del sistema de inventario.")
                print("")
                break

            if opcionProductos == "1":
                nombre = input("Ingresa el nombre del producto: ")
                try:
                    cantidad = int(input("Ingresa la cantidad: "))
                    precio = float(input("Ingresa el precio: "))
                    producto = Producto(nombre, cantidad, precio)
                    inventario.append(producto)
                    print("Producto agregado.")
                    print("")
                except ValueError:
                    print("Error: Entrada no válida.")
                    print("")
            elif opcionProductos == "2":
                for p in inventario:
                    print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                print("")
            elif opcionProductos == "3":
                nombre = input("Ingresa el nombre del producto a buscar: ")
                encontrado = False
                for p in inventario:
                    if p.nombre == nombre:
                        print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                        print("")
                        encontrado = True
                        break
                if not encontrado:
                    print("Producto no encontrado.")
                    print("")
            elif opcionProductos == "4":
                nombre = input("Ingresa el nombre del producto a actualizar: ")
                try:
                    nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                    for p in inventario:
                        if p.nombre == nombre:
                            p.cantidad = nueva_cantidad
                            print("Cantidad actualizada.")
                            print("")
                            break
                except ValueError:
                    print("Error: Entrada no válida.")
                    print("")
            elif opcionProductos == "5":
                nombre = input("Ingresa el nombre del producto a eliminar: ")
                for p in inventario:
                    if p.nombre == nombre:
                        inventario.remove(p)
                        print("Producto eliminado.")
                        print("")
                        break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                print("")

    if opcionMenuPrincipal == "4":
        class Tarea:
            def __init__(self, titulo, descripcion, estado):
                self.titulo = titulo
                self.descripcion = descripcion
                self.estado = estado

        def menuTarea():
            print("Sistema de Tareas")
            print("1. Agregar tarea")
            print("2. Mostrar tarea")
            print("3. Buscar tarea")
            print("4. Actualizar tarea")
            print("5. Eliminar tarea")
            print("0. Salir")
            print("")

        tareas = []

        while True:
            menuTarea()
            opcionTareas = input("Elige una opción del gestor de tareas: ")

            if opcionTareas == "0":
                print("Saliendo del gestor de tareas.")
                print("")
                break

            if opcionTareas == "1":
                titulo = input("Ingresa el titulo de la tarea: ")
                try:
                    descipcion = input("Ingresa descipcion de la tarea: ")
                    estado = "Pendiente"
                    tarea = Tarea(titulo, descipcion, estado)
                    tareas.append(tarea)
                    print("tarea agregada.")
                    print("")
                except ValueError:
                    print("Error: Entrada no válida.")
                    print("")
            elif opcionTareas == "2":
                for t in tareas:
                    print(f"Titulo: {t.titulo}, Descripcion: {t.descripcion}, Estado: {t.estado}")
                print("")
            elif opcionTareas == "3":
                titulo = input("Ingresa el titulo la tarea: ")
                encontrado = False
                for t in tareas:
                    if t.titulo == titulo:
                        print(f"Titulo: {t.titulo}, Descripcion: {t.descripcion}, estado: {t.estado}")
                        print("")
                        encontrado = True
                        break
                if not encontrado:
                    print("Tarea no encontrada.")
                    print("")
            elif opcionTareas == "4":
                titulo = input("Ingresa el titulo de la tarea: ")
                try:
                    for t in tareas:
                        if t.titulo == titulo:
                            t.estado = "Completada"
                            print("Estado actualizado.")
                            print("")
                            break
                except ValueError:
                    print("Error: Entrada no válida.")
                    print("")
            elif opcionTareas == "5":
                titulo = input("Ingresa el titulo de la tarea a eliminar: ")
                for t in tareas:
                    if t.titulo == titulo:
                        tareas.remove(t)
                        print("Tarea eliminada.")
                        print("")
                        break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                print("")
