from django.contrib import admin
from .models import Clients, Inspections


@admin.register(Clients)
class ClientsFormAdmin(admin.ModelAdmin):
    exclude = [
        "id"
    ]

    list_display = [
        "status",
        "first_name",
        "business_name",
        "date_added"
    ]


@admin.register(Inspections)
class InspectionsForAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "date",
        "completed",
        "date_added"
    ]
