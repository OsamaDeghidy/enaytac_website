from django.contrib import admin
from .models import Person
# Register your models here.
from django.utils.html import format_html
from django.urls import reverse

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_link', 'address', 'last_name','speciality')
    search_fields = ('name', 'phone_number', 'email', 'address', 'last_name','speciality')
    list_filter = ('address',)

    def email_link(self, obj):
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)

    email_link.short_description = 'email'


admin.site.register(Person, PersonAdmin)

