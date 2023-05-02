from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Tea
from django.utils.translation import gettext as _
# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),

    )
    readonly_fields = ('last_login',)
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff',
                    'is_superuser',

                )

            }
        ),
    )
    
    
class TeaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available', 'created_at']
    list_filter = ['is_available', 'created_at', 'name', 'price']
    search_fields = ['name', 'price', 'description']
    


admin.site.register(User, UserAdmin)
admin.site.register(Tea, TeaAdmin)
