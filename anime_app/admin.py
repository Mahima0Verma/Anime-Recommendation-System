from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class MahimaAdmin(UserAdmin):
    list_display = ('id','email','name','is_superuser',)
    list_filter = ('is_superuser',)
    fieldsets = (
        ('User Credentials',{'fields':('email','password',)}),
        ('Personal info',{'fields':('name',)}),
        ('Permissions',{'fields':('is_superuser',)}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','name','password1','password2'),
        }),

    )
    search_fields  = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

admin.site.register(NewUser,MahimaAdmin) 
admin.site.register(UserPreferences) 

# Register your models here.
