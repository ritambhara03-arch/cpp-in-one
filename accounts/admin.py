from django.contrib import admin

from accounts.cart.migrations.models import Profile
from .models import *
#Register your models here.

admin.site.register(Profile)