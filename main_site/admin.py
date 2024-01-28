from django.contrib import admin
from .models import Enquiries


@admin.register(Enquiries)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "telephone",
        "email",
        "property_type",
        "received"
    ]
