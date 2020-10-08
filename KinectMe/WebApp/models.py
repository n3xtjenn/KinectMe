from django.db import models
from django.contrib.auth.models import User
from djchoices import DjangoChoices, ChoiceItem

# Create your models here.

'''
class Selection(models.Model):
    ACTIVITY= (
        ("C", "Climbing"),
        ("S", "Soccer"),
        ("F", "Football"),
        ("U", "Ultimate Frisbee"),
        ("Y", "Yoga"),
        ("R", "Running"),
        ("B", "Basketball"),
        ("V", "Vollyball"),
        ("CY", "Cycling"),
        ("G", "Golf"),
        ("CO", "Cornhole"),
        ("BA", "Baseball"),
        ("SB", "Softball"),
        ("Z", "Zumba"),
        ("L", "Lifting"),
        ("G", "Golf"),
        ("CO", "Cornhole"),
        ("BA", "Baseball"),
)
    sport = models.CharField(max_length=15)
    def __str__(self):
        return self.sport
    '''
class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    age = models.CharField(max_length=2)
    #tag1 = models.MultipleChoiceField(max_length=15, choices=ACTIVITIES)

    class Selection(DjangoChoices):
        Soccer = ChoiceItem("Soccer")
        Vollyball = ChoiceItem("Vollyball")
        Climbing = ChoiceItem("Climbing")
        Football = ChoiceItem("Football")
        Zumba = ChoiceItem("Zumba")
        Yoga = ChoiceItem("Yoga")
        Running = ChoiceItem("Running")
        Golf = ChoiceItem("Golf")
        Cornhole = ChoiceItem("Cornhole")
        Ultimate = ChoiceItem("Ultimate")
        Basketball = ChoiceItem("Basketball")
        Softball = ChoiceItem("Softball")
        Lifting = ChoiceItem("Lifting")

    sport1 = models.CharField(max_length=20, choices=Selection.choices)
    sport2 = models.CharField(max_length=20, choices=Selection.choices)
    sport3 = models.CharField(max_length=20, choices=Selection.choices)

    def __str__(self):
        return self.user_name