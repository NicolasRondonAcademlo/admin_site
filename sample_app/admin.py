from datetime import datetime

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
    search_fields = ('name',)

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

    list_display = ('question_text','ref_author', 'pub_date', 'created_date', 'updated_date',
                    'has_been_published')
    list_display_links = ('ref_author',)
    list_editable = ('question_text',)
    date_hierarchy = 'pub_date'
    save_on_top = True
    list_filter = ('ref_author', 'pub_date')
    autocomplete_fields = ['ref_author']


    def has_been_published(self, obj):
        present =  datetime.now()
        return obj.pub_date.date() < present.date()

    has_been_published.boolean = True

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes', 'created_date', 'updated_date')
    list_filter = ('question__ref_author',)
    search_fields = ('choice_text','question__question_text', 'question__ref_author__name')


admin.site.register(Author,AuthorAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['name']})
#     ]
#
#     list_display = ('name', 'created_date', 'updated_date')
# En caso de usar esta manera debemos elminiar la linea admin.site.register(Author,AuthorAdmin)