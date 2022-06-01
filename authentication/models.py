from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    """ User Model Manager """
    def create_user(self, username, password=None, is_active=True):
        if not username:
            raise ValueError("L'utilisasteur doit avoir un nom d'utilisateur")
        if not password:
            raise ValueError("L'utilisateur doit avoir un mot de passe")
        # if not full_name:
        #     raise ValueError('User must have a full name')
        user_obj = self.model(
            username=username
        )
        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.save(using=self._db)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, through="review.UserFollows", related_name="user_followers", symmetrical=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [username]

    objects = UserManager()



