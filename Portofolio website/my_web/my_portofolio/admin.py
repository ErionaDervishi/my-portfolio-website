from django.contrib import admin
from .models import AboutMe, Contact_model, Project_model

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    search_fields = ('content',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('email',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')

admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Contact_model, ContactAdmin)
admin.site.register(Project_model, ProjectAdmin)
