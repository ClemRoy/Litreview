from django.contrib import admin

# Register your models here.

from review.models import UserFollows

admin.site.register(UserFollows)