from django.contrib import admin
from .models import Ucak, Parca, Takim, Personel, UretilenUcak
from django.contrib.auth.models import User

admin.site.register(Ucak)
admin.site.register(Parca)
admin.site.register(Takim)
class PersonelAdmin(admin.ModelAdmin):
    list_display = ['user', 'takim'] 
    fields = ['user', 'takim', 'sifre']

admin.site.register(Personel, PersonelAdmin)
admin.site.register(UretilenUcak)