from django.contrib import admin
from workstations.models import WorkStations


class WorkStationsAdmin(admin.ModelAdmin):
    list_display = ('id','worker','workstation_cycle_time','transportation_time','created_at',
                    'updated_at')
    search_fields = ('worker', 'workstation_cycle_time','transportation_time')
    readonly_fields = ('id', 'created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(WorkStations, WorkStationsAdmin)

