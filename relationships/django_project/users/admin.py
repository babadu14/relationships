from django.contrib import admin
from users.models import Citizen, Passport, UserProfile, Post,Event

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Passport)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Event)


