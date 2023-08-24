from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User

# Create your models here.
class PostHome(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to = 'OlavaFletesApp')
    created = models.DateTimeField(default=django.utils.timezone.now)
    updated = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.usuario.username