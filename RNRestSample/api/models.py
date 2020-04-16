from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    prodi = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.nim)
