from django.db import models
from django.utils import timezone

class Docentes(models.Model):
    Docente = models.CharField(max_length=100)

    def __str__(self):
        return self.Docente

class Cursos(models.Model):
    Curso = models.CharField(max_length= 100)
    Docente = models.CharField(max_length=100)
    Hora = models.TimeField()
    Fecha = models.DateField()
    Ingenieria = models.CharField(max_length=40)
    Aula = models.CharField(max_length=10)
    Url = models.CharField(max_length=100)


    def __str__(self):
        return self.Curso

class DocentesV2(models.Model):
    Docente = models.CharField(max_length= 100)

    def __str__(self):
        return self.Docente

class IngenieriaV2(models.Model):
    Ingenieria = models.CharField(max_length= 100)

    def __str__(self):
        return self.Ingenieria

class Horas(models.Model):
    Text = models.CharField(max_length= 100)
    Hora = models.TimeField()

    def __str__(self):
        return self.Text

class Fechas(models.Model):
    Text = models.CharField(max_length= 100)
    Fecha = models.DateField()

    def __str__(self):
        return self.Text

class CursosList(models.Model):
    Curso = models.CharField(max_length= 100)

    def __str__(self):
        return self.Curso

class Aulas(models.Model):
    Aula = models.CharField(max_length= 100)

    def __str__(self):
        return self.Aula

class CursosV2(models.Model):
    IdCurso = models.CharField(max_length=100)
    Curso = models.ForeignKey(CursosList, null=True, blank=True, on_delete=models.CASCADE)
    Docente = models.ForeignKey(DocentesV2, null=True, blank=True, on_delete=models.CASCADE)
    Hora = models.ForeignKey(Horas, null=True, blank=True, on_delete=models.CASCADE)
    Fecha= models.ForeignKey(Fechas, null=True, blank=True, on_delete=models.CASCADE)
    Ingenieria = models.ForeignKey(IngenieriaV2, null=True, blank=True, on_delete=models.CASCADE)
    Aula = models.ForeignKey(Aulas, null=True, blank=True, on_delete=models.CASCADE)
    Url = models.CharField(max_length=100)


    def __str__(self):
        return self.IdCurso

class Registros(models.Model):
    Nombre=models.CharField(max_length=100)
    ApellidoP=models.CharField(max_length=100)
    ApellidoM=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Curso = models.CharField(max_length=100)
    Docente = models.CharField(max_length=100)
    Hora = models.TimeField()
    Fecha = models.DateField()
    Aula = models.CharField(max_length=100)
    Ingenieria = models.CharField(max_length=100)

    def __str__(self):
        return str(str(self.Nombre) +  str(self.ApellidoP) + str(self.ApellidoM) + " | " +
            str(self.Email) + " | " + str(self.Curso)+ " | " + str(self.Docente)+ " | " + str(self.Ingenieria))

class Images(models.Model):
    Image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.Image)
        