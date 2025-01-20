import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF  # Para generar el PDF
from datetime import datetime  # Importar datetime para manejar fechas
import os
# Datos de ejemplo de habitaciones reservadas (simulación)
habitaciones_reservadas = {
    '101': False,
    '102': True,  # Esta habitación está ocupada
    '103': False,
    '104': False,
    '105': False,
    '106': False,
    '107': False,
    '108': False,
    '109': False,
    '110': False,
}

def verificar_disponibilidad():
    habitacion = entry_habitacion.get()  # Obtener el número de habitación ingresado
    if habitacion in habitaciones_reservadas:  # Verificar si la habitación existe
        if habitaciones_reservadas[habitacion]:  # Verificar si está reservada
            messagebox.showwarning("Ocupada", f"La habitación {habitacion} ya está reservada.")
        else:
            messagebox.showinfo("Disponible", f"La habitación {habitacion} está disponible.")
    else:
        messagebox.showerror("Error", "Número de habitación no válido")

def realizar_reserva():
    # Obtener los datos ingresados por el usuario
    nombre = entry_nombre.get()
    email = entry_email.get()
    habitacion = entry_habitacion.get()
    dias = int(entry_dias.get())
    precio_por_noche = 50  # Precio base por noche

    # Verificar si la habitación está disponible
    if habitaciones_reservadas.get(habitacion, True):  # True si la habitación no existe o está reservada
        messagebox.showwarning("Ocupada", f"La habitación {habitacion} ya está reservada.")
        return

    # Calcular el total a pagar
    total_pagar = dias * precio_por_noche

    # Guardar la reserva (simulación)
    habitaciones_reservadas[habitacion] = True  # Marcar habitación como reservada
    reserva = {
        "nombre": nombre,
        "email": email,
        "habitacion": habitacion,
        "dias": dias,
        "total_pagar": total_pagar,
    }

    # Generar el PDF
    generar_pdf(reserva)

    # Mostrar mensaje de éxito
    messagebox.showinfo("Reserva Exitosa", f"Reserva completada para {nombre}\nTotal a pagar: ${total_pagar}")

def generar_pdf(reserva):
    # Crear la carpeta "pdfs" si no existe
    if not os.path.exists("pdfs"):
        os.makedirs("pdfs")  # Crear la carpeta
    # Crear un nombre único para el archivo PDF
    fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")  # Formato: AñoMesDía_HoraMinutoSegundo
    pdf_path = f"pdfs/reserva_{reserva['nombre']}_{reserva['habitacion']}_{fecha_actual}.pdf"

    # Crear un PDF con los detalles de la reserva
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Agregar contenido al PDF
    pdf.cell(200, 10, txt="Detalles de la Reserva", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Nombre: {reserva['nombre']}", ln=True)
    pdf.cell(200, 10, txt=f"Correo Electrónico: {reserva['email']}", ln=True)
    pdf.cell(200, 10, txt=f"Habitación: {reserva['habitacion']}", ln=True)
    pdf.cell(200, 10, txt=f"Días de estadía: {reserva['dias']}", ln=True)
    pdf.cell(200, 10, txt=f"Total a pagar: ${reserva['total_pagar']}", ln=True)

    # Guardar el PDF
    pdf.output(pdf_path)
    messagebox.showinfo("PDF Generado", f"Se ha generado un PDF en: {pdf_path}")

# Configuración de la interfaz
tk_root = tk.Tk()
tk_root.title("Sistema Hotelero")
tk_root.geometry("400x400")

# Campos de entrada
tk.Label(tk_root, text="Nombre del Cliente:").pack()
entry_nombre = tk.Entry(tk_root)
entry_nombre.pack()

tk.Label(tk_root, text="Correo Electrónico:").pack()
entry_email = tk.Entry(tk_root)
entry_email.pack()

tk.Label(tk_root, text="Número de Habitación:").pack()
entry_habitacion = tk.Entry(tk_root)
entry_habitacion.pack()

# Botón para verificar disponibilidad
tk.Button(tk_root, text="Verificar Disponibilidad", command=verificar_disponibilidad).pack()

tk.Label(tk_root, text="Número de Días:").pack()
entry_dias = tk.Entry(tk_root)
entry_dias.pack()

# Botón para realizar la reserva
tk.Button(tk_root, text="Reservar Habitación", command=realizar_reserva).pack()

# Iniciar la interfaz gráfica
tk_root.mainloop()