from django.db import models

# Modelos
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    codigo = models.CharField(primary_key= True, max_length=4 )
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} en habitación {self.habitacion.numero}"