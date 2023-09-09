import tkinter as tk
import random

# Función para mostrar el mensaje de felicitaciones
def mostrar_felicidades():
    mensaje.config(text="¡Felicidades, De ahora en adelante perteneces a la comunidad LGBTIQ+, no te me arrimes !")

# Función para mover el botón "No" a una nueva ubicación
def mover_no(event):
    x = random.randint(50, 250)
    y = random.randint(50, 150)
    boton_no.place(x=x, y=y)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Selección")

# Configurar el color de fondo de la ventana
ventana.configure(bg="black")

# Crear un mensaje para pedir al jugador que seleccione un número
mensaje = tk.Label(ventana, text="¿ERES GAY?:", fg="green", bg="black", font=("Arial", 24))
mensaje.pack()

# Crear un botón "Sí" más grande que muestra felicitaciones al hacer clic
boton_si = tk.Button(ventana, text="SÍ", command=mostrar_felicidades, fg="green", bg="black", font=("Arial", 16))
boton_si.pack(pady=20)  # Añadir espacio entre el botón y el mensaje

# Crear un botón "No" más grande que mueve el botón "No" al hacer clic o al pasar el mouse
boton_no = tk.Button(ventana, text="NO", fg="green", bg="black", font=("Arial", 16))
boton_no.pack(pady=20)  # Añadir espacio entre el botón "No" y el botón "Sí"

# Colocar el botón "No" en una ubicación inicial aleatoria
mover_no(None)

# Asignar la función mover_no al evento Enter del botón "No"
boton_no.bind("<Enter>", mover_no)

ventana.mainloop()
