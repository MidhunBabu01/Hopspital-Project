from django.db import models

# Create your models here.

class Categories(models.Model):
    choices = (
        ("Dental Department", "Dental Department"),
        ("Surgical Department", "Surgical Department"),
        ("Neurological Department", "Neurological Department"),
        ("Ophthalmological Department", "Ophthalmological Department"),
    )
    department = models.CharField(max_length=250, choices=choices)
    small_desc = models.TextField()

    


    def __str__(self):
        return self.department









class Details(models.Model):
    def __str__(self):
        return self.department
    choices = (
        ("Dental Department", "Dental Department"),
        ("Surgical Department", "Surgical Department"),
        ("Neurological Department", "Neurological Department"),
        ("Ophthalmological Department", "Ophthalmological Department"),
    )
    department = models.CharField(max_length=250, choices=choices)
    hosptladrs = models.TextField()
    dprtimag = models.ImageField()
    small_desc = models.TextField()
    big_desc = models.TextField()
    doctor_name = models.CharField(max_length=250)
    doctor_img = models.ImageField(upload_to="pictures")
    doctor_detail = models.TextField()
    doctorname2 = models.CharField(max_length=250)
    doctorimg2 = models.ImageField(upload_to="pictures")
    doctordetail2 = models.TextField()



    
