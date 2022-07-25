from django.contrib import admin

# Register your models here.

from review.models import Ticket, UserFollows

admin.site.register(UserFollows)
admin.site.register(Ticket)