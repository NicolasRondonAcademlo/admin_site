from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.empty_value_display = "No valor"

class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = "Unknow"
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
    list_display_links = ('ref_author',)
    date_hierarchy = 'pub_date'
    save_on_top = True


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