from django.contrib import admin
from .models import Komarigotolist

from .models import Eikyo1
from .models import Eikyo2

from .models import Genin1
from .models import Genin2

# Register your models here.
admin.site.register(Komarigotolist)

admin.site.register(Eikyo1)
admin.site.register(Eikyo2)

admin.site.register(Genin1)
admin.site.register(Genin2)
