from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [username]
