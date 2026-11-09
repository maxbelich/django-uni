from django.db import models

class Professor(models.Model):
    professorName = models.CharField(max_length=30)

class Semester(models.Model):
    semester = models.CharField(max_length=20)

class Kurs(models.Model):
    kursName = models.CharField(max_length=20)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)

class Student(models.Model):
    studentName = models.CharField(max_length=30)
    kurse = models.ManyToManyField(Kurs)

class Studentenausweis(models.Model):
    ausweisnummer = models.CharField(max_length=12, unique=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

class Kursbeschreibung(models.Model):
    beschreibung = models.TextField()
    kurs = models.OneToOneField(Kurs, on_delete=models.CASCADE)