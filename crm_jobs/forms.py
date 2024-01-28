from django import forms
from . import models


class ClientForm(forms.ModelForm):
    """ Form for creating/updating inspections. """

    class Meta:
        model = models.Clients
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Required*"}),
            "telephone": forms.TextInput(attrs={"type": "tel", "placeholder": "Required*"}),
            "business_name": forms.TextInput(attrs={"placeholder": "Required*"}),
            "postcode": forms.TextInput(attrs={"placeholder": "Required*"})
        }


class ClientNoteForm(forms.ModelForm):
    """ Form for creating/updating inspections. """
    class Meta:
        model = models.Clients
        fields = ("notes",)

        widgets = {
            "notes": forms.Textarea(attrs={"placeholder": "Enter client notes here..."})
        }


class InspectionForm(forms.ModelForm):
    """ Form for creating/updating inspections. """

    class Meta:
        model = models.Inspections
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "placeholder": "Required"}),
            "fee": forms.NumberInput(attrs={"placeholder": "£"}),
            "notes": forms.Textarea(attrs={"placeholder": "Enter inspection notes here..."})
        }
