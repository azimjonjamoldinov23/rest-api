from django.contrib import admin
from .models import Students , Yonalish
# Register your models here.

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'fam']

@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']