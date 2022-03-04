from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
    ]

    list_display = ('name', 'created_date', 'updated_date')

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question information", {
            'fields': ('question_text',)
        }),
        (
            "Date", {
                "fields": ("pub_date",)
            }
        ),
        ('The author', {
            'classes': ('collapse',),
            'fields': ('ref_author',),
        })
    ]

    list_display = ('question_text','ref_author', 'pub_date', 'created_date', 'updated_date')
    list_display_links = ('question_text','ref_author',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['name']})
#     ]
#
#     list_display = ('name', 'created_date', 'updated_date')
# En caso de usar esta manera debemos elminiar la linea admin.site.register(Author,AuthorAdmin)