from django.db import models

class Profile(models.Model):
    DC_TEAMS = (
        ("DR", "Dresser-Rand").
        ("HF", "HeartFlow"),
        ("IL", "Instrumentation Laboratory"),
        ("MD", "Medtronic"),
        ("NOPS", "Northampton OPS"),
        ("ST", "Stantec"),
        ("SR", "Sterling Rope")
    )
    name = models.CharField(max_length=256) # Ask for both first + last
    DC_team = models.CharField(max_length=4, choices=DC_TEAMS) # change to dropdown
    work_location_name = models.CharField(max_length=128)
    work_city = models.CharField(max_length=128)
    work_state = models.CharField(max_length=128)
    work_country = models.CharField(max_length=128)
    start_date = models.DateField("Start date")
    email = models.EmailField(max_length=128)
    profile_pic = models.ImageField(upload_to='img/profile/%Y/%m/')
    message = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
