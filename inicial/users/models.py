from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    app = models.CharField(max_length=50, verbose_name='apellido paterno')
    apm = models.CharField(max_length=50, verbose_name='apellido materno')
    tel = models.CharField(max_length=10, null=True, verbose_name='telefono')
    email = models.EmailField(max_length=150, unique=True)
    add = models.CharField(max_length=250,verbose_name='dirección')

    class Meta:
        db_table = 'users'