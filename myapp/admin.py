from django.contrib import admin
from .models import Yonalish, Students


@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fam', 'yosh', 'kurs', 'yonalish')
    list_filter = ('kurs', 'yonalish')
    search_fields = ('name', 'fam')