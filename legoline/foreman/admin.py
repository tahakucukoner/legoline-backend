from django.contrib import admin
from foreman.models import ForemanInfo

class ForemanInfoAdmin(admin.ModelAdmin):
    list_display = ('id','user','worker_name','worker_surname','worker_tel_no','worker_task_time','worker_workstation','created_at',
                    'updated_at')
    search_fields = ('worker_name', 'worker_surname','worker_tel_no','worker_workstation')
    readonly_fields = ('id', 'created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(ForemanInfo, ForemanInfoAdmin)
