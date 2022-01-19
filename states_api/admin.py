from django.contrib import admin

from states_api.models import Governor, NigerianState, DeputyGovernor


class GovernorAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')


class NigerianStateAdmin(admin.ModelAdmin):
    list_display = ('name_of_state', 'number_of_local_governments', 'range_of_population')


class DeputyGovernorAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'governor')


admin.site.register(Governor, GovernorAdmin)
admin.site.register(NigerianState, NigerianStateAdmin)
admin.site.register(DeputyGovernor, DeputyGovernorAdmin)