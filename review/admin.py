from django.contrib import admin

# Register your models here.

from review.models import Review, Ticket, UserFollows

admin.site.register(UserFollows)
admin.site.register(Ticket)
admin.site.register(Review)
