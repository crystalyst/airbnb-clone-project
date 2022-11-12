from django.db import models
from django.contrib.auth.models import AbstractUser

#inherit everything from Django's basic Users
class User(AbstractUser):
    # choice
    class GenderChoices(models.TextChoices):
        # value will go to the DB / label that you will see on Admin panel
        MALE = ('male', 'Male')
        FEMALE = ('female', 'Female')

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won" # this can still make tuple
        USD = "usd", "US Dollar"
    # overwrite
    # editable -> does not show up on admin
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    avatar = models.ImageField(blank=True)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, )
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices, )
