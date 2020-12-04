from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Text)
admin.site.register(Photo)
admin.site.register(Avatar)

class AvatarInline(admin.TabularInline):
    model = Avatar
