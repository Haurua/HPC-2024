from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Enquiries
        fields = [
            "name",
            "telephone",
            "email",
            "postcode",
            "property_type",
            "description"
        ]

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Required*"}),
            "telephone": forms.TextInput(attrs={"placeholder": "Required*", "type": "tel"}),
            "email": forms.EmailInput(attrs={"placeholder": "Required*"}),
            "postcode": forms.TextInput(attrs={"placeholder": "Required*"}),
            "description": forms.Textarea(attrs={"placeholder": "Required*"}),
        }
