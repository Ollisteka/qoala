from django.contrib import admin
from . import models

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'token'),
        'login',
        'is_active',
        ('is_staff', 'is_superuser'),
        'last_login',
        'in_scoreboard',
        'group'
#        'password',
    )
    list_display = ('name', 'login', 'is_active', 'is_staff', 'is_superuser', 'in_scoreboard', 'group')
    list_editable = ('is_active', 'login', 'is_staff', 'is_superuser', 'in_scoreboard', 'group')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'group')

    search_fields = ('name', 'login', 'group')
    readonly_fields = ('last_login', 'password')

admin.site.register(models.Team, TeamAdmin)