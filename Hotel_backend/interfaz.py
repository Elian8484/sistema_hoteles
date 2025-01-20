import tkinter as tk 
import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
import os

# Datos de ejemplo de habitaciones reservadas (simulación)
habitaciones_reservadas = {
    '101': False,
    '102': True,  # Esta habitación está ocupada
    '103': False,
}

def verificar_disponibilidad():
    habitacion = entry_habitacion.get()
    if habitacion in habitaciones_reservadas:
        if habitaciones_reservadas[habitacion]:
            messagebox.showwarning("Ocupada", f"La habitación {habitacion} ya está reservada.")
        else:
            messagebox.showinfo("Disponible", f"La habitación {habitacion} está disponible.")
    else:
        messagebox.showerror("Error", "Número de habitación no válido")

def realizar_reserva():
    nombre = entry_nombre.get()
    email = entry_email.get()
    habitacion = entry_codigo.get()
    dias = int(entry_dias.get())
    precio_por_noche = 50  # Precio base por noche

    if habitaciones_reservadas.get(habitacion, True):
        messagebox.showwarning("Ocupada", f"La habitación {habitacion} ya está reservada.")
        return

    total_pagar = dias * precio_por_noche
    habitaciones_reservadas[habitacion] = True  # Marcar habitación como reservada

 generar_comprobante(nombre,codigo, dias, total_pagar)
    messagebox.showinfo("Reserva Exitosa", f"Reserva completada para {nombre}\nTotal a pagar: ${total_pagar}")

def generar_comprobante(nombre, habitacion, dias, total_pagar):
    archivo = f"comprobante_{nombre}.pdf"
    c = canvas.Canvas(archivo)
    c.drawString(100, 750, "Comprobante de Reserva")
    c.drawString(100, 730, f"Nombre: {nombre}")
    c.drawString(100, 710, f"Habitación: {codigo}")
    c.drawString(100, 690, f"Días: {dias}")
    c.drawString(100, 670, f"Total a pagar: ${total_pagar}")
    c.save()
    os.system(f"start {archivo}")  # Abre el PDF automáticamente

