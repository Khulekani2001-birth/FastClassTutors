from django.db import models
from django import forms
# Create your models here.

class Tutor(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    cell = models.CharField(max_length=128)
    email = models.EmailField()
    id_or_passport = models.CharField(max_length=256)

    academic_year = models.CharField(max_length=64)
    degree_or_major = models.CharField(max_length=128)
    number_of_hours = models.CharField(max_length=16)
   
    #Matric Subjects and Symbols
    Accounting = models.CharField(max_length=3, default="NA")
    Afrikaans_Second_Language = models.CharField(max_length=3, default="NA")
    Biology_or_Life_Sciences = models.CharField(max_length=3, default="NA")
    Business = models.CharField(max_length=3, default="NA")
    Chemistry = models.CharField(max_length=3, default="NA")
    Economics = models.CharField(max_length=3, default="NA")
    English = models.CharField(max_length=3, default="NA")
    Geography = models.CharField(max_length=3, default="NA")
    History = models.CharField(max_length=3, default="NA")
    ICT = models.CharField(max_length=3, default="NA")
    isiXhosa = models.CharField(max_length=3, default="NA")
    Mathematics = models.CharField(max_length=3, default="NA")
    Mathematics_AP = models.CharField(max_length=3, default="NA")
    Physical_Sciences = models.CharField(max_length=3, default="NA")
    Other_1 = models.CharField(max_length=256, default="NA")
    Other_2 = models.CharField(max_length=256, default="NA")

    def __str__(self):
        return self.name +" "+self.surname

class CsvImportForm(forms.Form):
    upload_csv = forms.FileField()