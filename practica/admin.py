__author__ = 'Manuel'

from django.contrib import admin

from .models import Transaccion

class TransaccionAdmin(admin.ModelAdmin):
    readonly_fields = ['order']
    pass

admin.site.register(Transaccion, TransaccionAdmin)