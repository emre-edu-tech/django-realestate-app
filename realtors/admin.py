from django.contrib import admin
from .models import Realtor    #.models is coming from the above code admin

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name') # here only id link is bold on the frontend
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
