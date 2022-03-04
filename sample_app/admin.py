from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
    ]

    list_display = ('name', 'created_date', 'updated_date')


admin.site.register(Author,AuthorAdmin)
admin.site.register(Question)
admin.site.register(Choice)