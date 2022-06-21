from django.contrib import admin

# Register your models here.

from .models import Recepy
from .models import User

admin.site.register(Recepy)
admin.site.register(User)