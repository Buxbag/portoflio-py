import schedule
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from plyer import notification
from kivy.uix.spinner import Spinner

# Diccionario para almacenar las tareas
tareas = {
    'diarias': [],
    'semanales': [],
    'mensuales': []
}

# Función para agregar una tarea con día y hora especificada
def agregar_tarea(tipo, tarea, dia=None, hora="09:00"):
    if tipo in tareas:
        tareas[tipo].append((tarea, dia, hora))
        print(f"Tarea '{tarea}' agregada a {tipo}. Día: {dia}, Hora: {hora}.")
    else:
        print("Tipo de tarea no reconocido. Usa 'diarias', 'semanales' o 'mensuales'.")

# Función para programar recordatorios
def programar_recordatorios():
    for tipo, lista in tareas.items():
        for tarea, dia, hora in lista:
            if tipo == 'diarias':
                schedule.every().day.at(hora).do(notificar, tarea, tipo)
            elif tipo == 'semanales':
                if dia:
                    getattr(schedule.every(), dia).at(hora).do(notificar, tarea, tipo)
            elif tipo == 'mensuales':
                schedule.every().day.at(hora).do(verificacion_y_notificacion_mensual, tarea, dia)

#Función de notificación
def notificar(tarea, tipo):
    notification.notify(
        title=f'Recordatorio {tipo.capitalize()}',
        message=tarea,
        timeout=10
    )

#Función para verificar y notificar tareas mensuales
def verificacion_y_notificacion_mensual(tarea, dia):
    if datetime.now().day == int(dia):
        notificar(tarea, 'mensuales')

programar_recordatorios()

class RecordatorioApp(App):
    def build(self):
        self.title = 'Recordatorios'

        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Añade una tarea")
        layout.add_widget(self.label)

        self.textinput = TextInput(hint_text="Escribe tu tarea aquí")
        layout.add_widget(self.textinput)

        self.spinner_tipo = Spinner(
            text='diarias',
            values=('diarias', 'semanales', 'mensuales')
        )
        layout.add_widget(self.spinner_tipo)

        self.spinner_dia_semana = Spinner(
            text='lunes',
            values=('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'),
            disabled=True
        )
        layout.add_widget(self.spinner_dia_semana)

        self.spinner_dia_mes = Spinner(
            text='1',
            values=tuple(str(i) for i in range(1, 32)),
            disabled=True
        )
        layout.add_widget(self.spinner_dia_mes)

        self.textinput_hora = TextInput(hint_text="Hora (HH:MM)")
        layout.add_widget(self.textinput_hora)

        self.button = Button(text="Agregar Tarea")
        self.button.bind(on_press=self.agregar_tarea)
        layout.add_widget(self.button)

        self.spinner_tipo.bind(text=self.on_spinner_tipo_change)

        return layout

    def on_spinner_tipo_change(self, spinner, text):
        if text == 'semanales':
            self.spinner_dia_semana.disabled = False
            self.spinner_dia_mes.disabled = True
        elif text == 'mensuales':
            self.spinner_dia_semana.disabled = True
            self.spinner_dia_mes.disabled = False
        else:
            self.spinner_dia_semana.disabled = True
            self.spinner_dia_mes.disabled = True

    def agregar_tarea(self, instance):
        tarea = self.textinput.text
        tipo = self.spinner_tipo.text
        dia = None
        if tipo == 'semanales':
            dia = self.spinner_dia_semana.text
        elif tipo == 'mensuales':
            dia = self.spinner_dia_mes.text
        hora = self.textinput_hora.text if self.textinput_hora.text else "09:00"

        if tarea:
            agregar_tarea(tipo, tarea, dia, hora)
            programar_recordatorios()
            self.label.text = f"Tarea '{tarea}' agregada. Día: {dia}, Hora: {hora}."
            self.textinput.text = ""
            self.textinput_hora.text = ""

if __name__ == '__main__':
    RecordatorioApp().run()
    while True:
        schedule.run_pending()
        time.sleep(1)