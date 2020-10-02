from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    fields = ['last_name', 'first_name']

admin.site.register(Person, PersonAdmin)


admin.site.site_header = "POLLSAPP Admin"
admin.site.site_title  = "POLLSAPP Admin Portal"
admin.site.index_title = "Welcome to POLLSAPP Portal"