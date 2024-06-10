from django.contrib import admin

# Register your models here.

from .models import Festival
from .models import Localizacao
from .models import Banda


admin.site.register(Festival)
admin.site.register(Localizacao)
admin.site.register(Banda)
