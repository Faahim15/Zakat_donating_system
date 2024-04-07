from django.contrib import admin
from . import models
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','description','progress','goal'] 


admin.site.register(models.Projects, ProjectAdmin) 
admin.site.register(models.BlogPost)
admin.site.register(models.Donations) 