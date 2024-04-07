from django.contrib import admin
from . import models
# Register your models here.
class DonatorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'gender','mobile_no','country']
    
    def first_name(self,obj):
        return obj.donator.first_name
    
    def last_name(self,obj):
        return obj.donator.last_name
    
    
admin.site.register(models.Donator, DonatorAdmin)