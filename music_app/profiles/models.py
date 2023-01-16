from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    INVALID_NAME_MESSAGE = "Ensure this value contains only letters, numbers, and underscore."
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            RegexValidator(regex='(^[A-Za-z0-9_]+$)', message=INVALID_NAME_MESSAGE),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )


    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(0),
        ),
    )
