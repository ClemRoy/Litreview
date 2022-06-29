from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    """ User Model Manager """
    def create_user(self, username, password=None, is_active=True):
        if not username:
            raise ValueError("L'utilisasteur doit avoir un nom d'utilisateur")
        if not password:
            raise ValueError("L'utilisateur doit avoir un mot de passe")
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.is_active = is_active
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, through="review.UserFollows", related_name="user_followers", symmetrical=False)

    USERNAME_FIELD = "username"

    objects = UserManager()



