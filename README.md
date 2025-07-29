SISTEMA CINEFÁCIL

- DESCRIPCIÓN DEL SISTEMA:
El programa CINEFÁCIL es una aplicación interactiva desarrollada en Python que permite a los usuarios:

    Registrar reservas de boletos de cine seleccionando película y horario.
    Visualizar todas las reservas realizadas.
    Cancelar reservas específicas.
    Modificar el precio del boleto.
    Agregar nuevos horarios a las películas existentes.

Está diseñado con funciones anidadas para mantener una estructura organizada y reutilizable, y se apoya en diccionarios y listas para gestionar los datos de las películas y las reservas.

- LISTA DE FUNCIONES DEL PROGRAMA:
A continuación, se describen las funciones internas de reserva():

    registro_de_pelicula():	Solicita al usuario su nombre, la película y el horario. Verifica que los datos sean válidos.
    compra_de_boletos():	Permite ingresar la cantidad de boletos y calcula el total según el precio.
    mostrar_reserva():	Muestra un resumen de la reserva realizada y la guarda en la lista reservas.
    reservas_hechas():	Imprime en pantalla todas las reservas registradas.
    cancelar_reserva():	Permite cancelar reservas por nombre, película y horario. Maneja casos donde hay más de una reserva por nombre.
    cambio_precio_boleto():	Permite al usuario cambiar el precio del boleto, con validación de entrada.
    nuevo_horario():	Agrega un nuevo horario a una película existente y lo ordena.

- CREACIÓN DE NUEVA RAMA:
  Utilizando los mismos comandos vistos en clase (git add . - git push - git branch)
  Agregar el uso de la función "git checkout -b NOMBRE DE LA RAMA"

- USO DE MERGE:
  1. Cambiar la rama principal (main): git checkout main
  2. Hacer merge con la rama creada: git merge NOMBRE DE LA RAMA
  3. Subir los cambios a GitHub: git push origin main

- ¿QUÉ APRENDÍ SOBRE GIT Y GITHUB?
Durante el desarrollo de este proyecto y su gestión con Git y GitHub, aprendí lo siguiente:

  Git me permite tener un control de versiones del código. Esto significa que puedo volver a versiones anteriores si cometo errores, sin perder el progreso.
  Las ramas son útiles para trabajar en nuevas funciones sin afectar la versión estable del proyecto.
  El merge permite combinar los cambios hechos en una rama secundaria con la rama principal, integrando las nuevas características.
  GitHub es una plataforma en la nube que facilita el almacenamiento de proyectos, colaboración en equipo y acceso desde cualquier lugar.
  Usar Git y GitHub me hace más organizado, evita errores fatales y me prepara para el trabajo colaborativo profesional.
