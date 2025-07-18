from django.contrib import admin

from .models import Achievement, Cat

admin.site.empty_value_display = 'Не задано'


class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class CatAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'color',
        'birth_year'
    )


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Cat, CatAdmin)
