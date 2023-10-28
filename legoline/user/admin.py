from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('id','name','surname','username', 'email', 'username', 'created_at',
                    'updated_at')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, CustomUserAdmin)
