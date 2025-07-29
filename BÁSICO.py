#Hecho por: ARENZ PELÁEZ - 1556425

# Diccionario de funciones y horarios de películas
funciones = {
    'Superman': ['10:00', '12:30', '15:00'],
    'Batman': ['11:00', '13:30', '16:00'],
    'Spiderman': ['10:30', '13:00', '15:30'],
    'Ironman': ['12:00', '14:30', '17:00'],
}

# Lista para almacenar las reservas
reservas = []

# Función principal para manejar las reservas
def reserva():

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
        print("Precio: Q50 c/u")

        # Validar la cantidad de boletos ingresada
        while True:
            cantidad = input("Cantidad de boletos (en números): ").strip()
            if cantidad.isdigit():
                break
            print("Dato inválido, ingresa nuevamente")
        
        # Calcular el total a pagar
        total = int(cantidad) * 50
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
    
    # Retornar las funciones para su uso afuera de la función principal
    return registro_de_pelicula, compra_de_boletos, mostrar_reserva, reservas_hechas


# Obtener las funciones
registro, compra, resumen, reserva = reserva()

print("CINEFÁCIL")

# Bucle principal del programa
while True:
    print("\nMENÚ")
    print("1.Adquirir entradas")
    print("2.Mostrar reservas")
    print("3.Salir")
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
        print("\n¡GRACIAS POR USAR CINEFÁCIL!")
        break

    else: 
        print("\nOPCIÓN INVÁLIDA, INTENTE NUEVAMENTE")