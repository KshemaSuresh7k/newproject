import imp
from django.contrib import admin
from .models import eventadd, studreg
from .models import parreg
from .models import addteach,leave

# Register your models here.

admin.site.register(studreg)
admin.site.register(parreg)
admin.site.register(addteach)
admin.site.register(eventadd)
admin.site.register(leave)

