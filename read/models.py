from django.db import models


class MyModel(models.Model):
    file = models.FileField(upload_to='uploads/')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.date)


    class Meta:
        verbose_name = "Fayllar_"



class DataFile(models.Model):
    path = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.path
