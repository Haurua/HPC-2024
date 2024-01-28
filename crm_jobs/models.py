from django.db import models
import uuid


class Clients(models.Model):
    status_choices = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=30, choices=status_choices, default="ACTIVE", verbose_name="Status")
    first_name = models.CharField(max_length=30, blank=False, verbose_name="First Name")
    last_name = models.CharField(max_length=30, blank=True, verbose_name="Last Name")
    telephone = models.CharField(max_length=12, blank=False, verbose_name="Telephone")
    telephone_alt = models.CharField(max_length=12, blank=True, verbose_name="Alternative Telephone")
    email = models.EmailField(max_length=30, blank=True, verbose_name="Email")
    position = models.CharField(max_length=30, blank=True, verbose_name="Position")
    business_name = models.CharField(max_length=30, blank=False, verbose_name="Business Name")
    address_line_1 = models.CharField(max_length=50, blank=True, verbose_name="Address Line 1")
    address_line_2 = models.CharField(max_length=50, blank=True, verbose_name="Address Line 2")
    city = models.CharField(max_length=20, blank=True, verbose_name="City")
    postcode = models.CharField(max_length=12, blank=False, verbose_name="Postcode")
    notes = models.TextField(null=True, blank=True, verbose_name="Client Notes")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["status"]
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Inspections(models.Model):
    completed_choices = [
        ("NO", "No"),
        ("YES", "Yes"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=False, blank=False)
    fee = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2, verbose_name="Inspection Fee")
    date = models.DateField(null=False, blank=False, verbose_name="Inspection Date")
    notes = models.TextField(null=True, blank=True, verbose_name="Job Notes")
    completed = models.CharField(max_length=30, choices=completed_choices, default="NO", verbose_name="Completed(?)")
    paid = models.CharField(max_length=30, choices=completed_choices, default="NO", verbose_name="Paid(?)")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.first_name

    class Meta:
        ordering = ["-date"]
        verbose_name = "Inspection"
        verbose_name_plural = "Inspections"
