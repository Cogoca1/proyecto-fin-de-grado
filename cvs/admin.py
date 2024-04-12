

# Register your models here.
from django.contrib import admin

from .models import Experiencia
from .models import Persona

admin.site.register(Experiencia)
admin.site.register(Persona)
