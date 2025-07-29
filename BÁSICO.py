#Hecho por: ARENZ PELÁEZ - 1556425

# Diccionario de funciones y horarios de películas
funciones = {
    'Superman': ['10:00', '12:30', '15:00'],
    'Batman': ['11:00', '13:30', '16:00'],
    'Spiderman': ['10:30', '13:00', '15:30'],
    'Ironman': ['12:00', '14:30', '17:00'],
}

# Lista para almacenar las reservas
reservas = [
    {'nombre':'Arenz', 'pelicula': 'Superman', 'horario': '10:00', 'boletos':5, 'total':250},
    {'nombre':'Juan', 'pelicula': 'Batman', 'horario': '16:00', 'boletos':2, 'total':100},
    {'nombre':'Pedro', 'pelicula': 'Ironman', 'horario': '17:00', 'boletos':1, 'total':50},
    {'nombre':'Arenz', 'pelicula': 'Batman', 'horario': '11:00', 'boletos':5, 'total':250}
]

# Función principal para manejar las reservas
def reserva():
    precio_boleto = 50.00
    # Funciones internas para manejar el registro, compra y resumen de reservas
    def registro_de_pelicula():

        # Registro de película y horario, incluyendo validaciones para evitar entradas vacías
        while True: 
            nombre = input("Ingresa tu nombre: ").strip().title()
            if nombre.strip():
                break
            print("CAMPO OBLIGATORIO")
            
        print("\nELIGE TU PELÍCULA")
        # Mostrar las películas y sus horarios disponibles
        for pelicula, horarios in funciones.items():
            print(f"\t{pelicula}: {', '.join(horarios)}")
        
        #  Pedir al usuario que ingrese la película, el horario y validar cada entrada
        while True:
            pelicula = input("\nIngrese el nombre de la película: ").title()
            if pelicula.strip():
                if pelicula in funciones:
                    break
                print("Película no disponible.")
                continue
            print("CAMPO OBLIGATORIO")
            
        while True:
            horario = input(f"Ingrese el horario para {pelicula} (opciones: {', '.join(funciones[pelicula])}): ")
            if horario.strip():
                if horario in funciones[pelicula]:
                    break
                print("Horario no disponible.")
                continue    
            print("CAMPO OBLIGATORIO")

        # Retornar los datos ingresados
        return nombre, pelicula, horario
    
    # Función para manejar la compra de boletos
    def compra_de_boletos():
        print("\nADQUIERE TUS BOLETOS")
        print(f"Precio: {precio_boleto:.2f} c/u")

        # Validar la cantidad de boletos ingresada
        while True:
            cantidad = input("Cantidad de boletos (en números): ").strip()
            if cantidad.isdigit():
                break
            print("Dato inválido, ingresa nuevamente")
        
        # Calcular el total a pagar
        total = int(cantidad) * precio_boleto
        # Retornar la cantidad de boletos y el total
        return cantidad, total
    
    # Función para mostrar el resumen de la reserva
    def mostrar_reserva(nombre, pelicula, horario, cantidad, total):
        print(f"\nRESUMEN DE LA RESERVA DE '{nombre.upper()}'")
        print(f"\tPelícula: {pelicula}")
        print(f"\tHorario: {horario}")
        print(f"\tTotal a pagar: Q{total}")

        # Crear un diccionario para almacenar la reserva y agregarlo a la lista de reservas
        reserva = {'nombre':nombre, 'pelicula': pelicula, 'horario': horario, 'boletos':cantidad, 'total':total}
        reservas.append(reserva)
    
    # Función para mostrar todas las reservas realizadas hasta el momento
    def reservas_hechas():
        print("\nRESERVAS")
        for i, reserva in enumerate(reservas, 1):
            print(f"\t{i} → Nombre: {reserva['nombre']} - Película: {reserva['pelicula']} - Horario: {reserva['horario']} - Boletos: {reserva['boletos']} - Total: Q{reserva['total']}")
            
    def cancelar_reserva():
        print("\nCANCELAR RESERVA")

        # Pedir nombre del usuario de la reserva a cancelar y validar la entrada
        while True: 
            nombre = input("Nombre: ").strip().title()
            if nombre.strip():
                break
            print("CAMPO OBLIGATORIO")

        # Busca en la lista de reservas las reservaciones del usuario y las cuenta
        encontrado = False 
        i = 0
        for reserva in reservas:
            if nombre in reserva['nombre']:
                i += 1

        if i > 1:
            # Mostrar las reservas del usuario
            print(f"\nRESERVAS DE '{nombre.upper()}'")
            for reserva in reservas:
                if nombre in reserva['nombre']:
                    print(f"\t{i} → Nombre: {reserva['nombre']} - Película: {reserva['pelicula']} - Horario: {reserva['horario']} - Boletos: {reserva['boletos']} - Total: Q{reserva['total']}") 
        
            while True: 
                pelicula = input("\nPelícula: ").title()
                if pelicula.strip():
                    break
                print("CAMPO OBLIGATORIO")
            while True: 
                horario = input("Horario: ")
                if horario.strip():
                    break
                print("CAMPO OBLIGATORIO")
                
            for j, reserva in enumerate(reservas):
                if {pelicula, horario}.issubset(reserva.values()):
                    del reservas[j]
                    encontrado = True
            
        elif i == 1:
            for j, reserva in enumerate(reservas):
                if nombre in reserva.values():
                    del reservas[j]
                    encontrado = True

        # Si no se encuentra la reserva, se informa al usuario
        if not encontrado:
            print('\nReserva no encontrada')
        else:
            print("\nRESERVA CANCELADA")
            
    def cambio_precio_boleto():
        nonlocal precio_boleto
        print("\nCAMBIO DE PRECIO DEL BOLETO")
        
        while True:
            cambio = input("Nuevo precio (en números): ")
            try:
                if float(cambio):
                    precio_boleto = float(cambio)
                    break
            except:
                print("\nENTRADA INVÁLIDA")
        
        print("\nCAMBIO DE PRECIO EXITOSO")
            
    def nuevo_horario():
        print("\nAGREGA NUEVO HORARIO")
        while True:
            pelicula = input("Ingrese el nombre de la película: ").title()
            if pelicula.strip():
                if pelicula in funciones:
                    break
                print("Película no encontrada")
                continue
            print("CAMPO OBLIGATORIO")
            
        while True:
            n_horario = input("Nuevo horario: ")
            if n_horario.strip():
                break
            print("CAMPO OBLIGATORIO")
            
        funciones[pelicula].append(n_horario)
        funciones[pelicula].sort()
        
        print(f'\n{pelicula} → {funciones[pelicula]}')
        print(f"\nNUEVO HORARIO AGREGADO")

    # Retornar las funciones para su uso afuera de la función principal
    return registro_de_pelicula, compra_de_boletos, mostrar_reserva, reservas_hechas, cancelar_reserva, cambio_precio_boleto, nuevo_horario


# Obtener las funciones
registro, compra, resumen, reserva, cancelar, cambio_precio, horario = reserva()

print("CINEFÁCIL")

# Bucle principal del programa
while True:
    print("\nMENÚ")
    print("1.Adquirir entradas")
    print("2.Mostrar reservas")
    print("3.Cancelar reserva")
    print("4.Cambiar precio de boletos")
    print("5.Agregar horario")
    print("6.Salir")
    opcion = input("Selecciona una opcion (por número): ")
    
    if opcion == '1':
        print("\nADQUIERE TUS ENTRADAS")
        nombre, pelicula, horario = registro()
        cantidad, total = compra()
        resumen(nombre, pelicula, horario, cantidad, total)
        
    elif opcion == '2':
        if len(reservas) != 0:
            reserva()
            continue
            
        print("\nNO HAY RESERVAS AÚN")
    
    elif opcion == '3':
        if len(reservas) != 0:
            cancelar()
            continue
            
        print("\nNO HAY RESERVAS AÚN")
    
    elif opcion == '4':
        cambio_precio()
    
    elif opcion == '5':
        horario()

    elif opcion == '6':
        print("\n¡GRACIAS POR USAR CINEFÁCIL!")
        break

    else: 
        print("\nOPCIÓN INVÁLIDA, INTENTE NUEVAMENTE")