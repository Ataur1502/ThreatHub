
from django.db import models

class Music(models.Model):
    id = models.AutoField(primary_key=True)
    artist=models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return f"Music {self.id}"
