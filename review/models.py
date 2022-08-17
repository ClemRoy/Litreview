from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

from PIL import Image


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    review_count = models.IntegerField(default=0, null=False, blank=True)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        if not self.image:
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
            self.resize_image()

    def __str__(self):
        return "Ticket"


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Review"


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="following",
                             on_delete=models.CASCADE)
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="followed_by",
        on_delete=models.CASCADE)

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )

    def __str__(self):
        return "UserFollow"
