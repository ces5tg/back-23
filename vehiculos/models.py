from django.db import models

class Vehiculo(models.Model):
    vehiculo_id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=20)
    kilometraje = models.FloatField()
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    #image = models.ImageField('imagen' , upload_to="image/", null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_vehiculo'

class VehiculoDocumento(models.Model):
    documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    fecha_vencimiento = models.DateField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    #archivo = models.FileField(upload_to="documentos/" , null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_vehiculo_documento'
