from django.db import models


class Enquiries(models.Model):
    property_choices = [
        ("COMMERCIAL", "Commercial"),
        ("INDUSTRIAL", "Industrial"),
        ("RESIDENTIAL", "Residential"),
    ]

    name = models.CharField(max_length=30, blank=False, verbose_name="Client Name")
    telephone = models.CharField(max_length=12, blank=False, verbose_name="Client Telephone")
    email = models.EmailField(blank=False, verbose_name="Client Email")
    postcode = models.CharField(max_length=12, blank=False, verbose_name="Client Postcode")
    property_type = models.CharField(max_length=12, blank=False, choices=property_choices, default="COMMERCIAL",
                                     verbose_name="Client Property")
    description = models.TextField(blank=False, verbose_name="Client Description")
    received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
