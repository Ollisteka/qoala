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


class TeamLoginAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'logged_at', 'ip_address')
    list_filter = ('team__name', )

    search_fields = ('team__login', 'team__name', 'ip_address')

    readonly_fields = ('logged_at', )

    def team_name(self, obj):
        return obj.team.name


admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.TeamLogin, TeamLoginAdmin)