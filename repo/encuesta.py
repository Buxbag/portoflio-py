import tkinter as tk
from tkinter import messagebox

# Definir las preguntas y respuestas
preguntas = [
    "¿Qué tan activo eres?",
    "¿Te gusta pasar tiempo al aire libre?",
    "¿Prefieres perros grandes o pequeños?",
    "¿Qué tan importante es la inteligencia del perro para ti?"
]

# Cada pregunta tiene su propio conjunto de respuestas
respuestas = [
    {1: "Muy poco activo", 2: "Poco activo", 3: "Bastante activo", 4: "Muy activo"},
    {1: "No me gusta", 2: "Me gusta un poco", 3: "Me gusta bastante", 4: "Me encanta"},
    {1: "Prefiero perros muy pequeños", 2: "Prefiero perros pequeños", 3: "Prefiero perros grandes", 4: "Prefiero perros muy grandes"},
    {1: "No es importante", 2: "Poco importante", 3: "Bastante importante", 4: "Muy importante"}
]

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("IdealistDog")

# Iniciar la puntuación
puntuacion_total = 0
respuestas_usuario = []

# Función para manejar la respuesta y pasar a la siguiente pregunta
def siguiente_pregunta(respuesta):
    global puntuacion_total
    puntuacion_total += respuesta
    respuestas_usuario.append(respuesta)
    if len(respuestas_usuario) < len(preguntas):
        mostrar_pregunta(len(respuestas_usuario))
    else:
        determinar_raza()

# Función para mostrar cada pregunta
def mostrar_pregunta(indice):
    pregunta = preguntas[indice]
    pregunta_label.config(text=pregunta)
    for i, (key, value) in enumerate(respuestas[indice].items()):
        botones_respuesta[i].config(text=value, command=lambda k=key: siguiente_pregunta(k))

# Función para determinar la raza de perro según la puntuación total
def determinar_raza():
    if puntuacion_total <= 8:
        raza = "Chihuahua"
    elif puntuacion_total <= 12:
        raza = "Beagle"
    elif puntuacion_total <= 16:
        raza = "Golden Retriever"
    else:
        raza = "Border Collie"
    
    messagebox.showinfo("Resultado", f"Tu raza de perro ideal es: {raza}")
    ventana.destroy()

# Crear widgets para mostrar las preguntas y respuestas
pregunta_label = tk.Label(ventana, text="", wraplength=12000, font=("Verdana", 14))
pregunta_label.pack(pady=20)

botones_respuesta = [tk.Button(ventana, text="", font=("Verdana", 12)) for _ in range(4)]
for boton in botones_respuesta:
    boton.pack(pady=5)

# Mostrar la primera pregunta
mostrar_pregunta(0)

# Iniciar el bucle de la aplicación
ventana.mainloop()

