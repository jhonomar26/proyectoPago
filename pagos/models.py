from django.db import models


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)  # Campo de identificación automático
    nomUsuario = models.CharField(max_length=100, null=True)
    totalIngresos = models.PositiveIntegerField(null=True)
    totalEgreso = models.PositiveIntegerField(null=True)
    totalGanancias = models.FloatField(null=True)
    correoElectronico = models.EmailField(max_length=254, null=True)
    def __str__(self):
        return self.nomUsuario or str(self.idUsuario)


class Egreso(models.Model):
    id = models.AutoField(primary_key=True)  # Campo id como clave primaria
    Usuario_idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaIngreso = models.DateField(null=True)
    monto = models.FloatField(null=True)
    categoria = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    def __str__(self):
        return f"Egreso de  {self.Usuario_idUsuario.nomUsuario}, fecha: {self.fechaIngreso}"


class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)  # Campo id como clave primaria
    Usuario_idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaIngreso = models.DateField(null=True)
    monto = models.FloatField(null=True)
    categoria = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    def __str__(self):
        return f"Ingreso de {self.Usuario_idUsuario.nomUsuario} - {self.fechaIngreso}"
