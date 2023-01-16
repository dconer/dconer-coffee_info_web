from django.contrib import admin
# including portfolio app in the admin
from .models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
