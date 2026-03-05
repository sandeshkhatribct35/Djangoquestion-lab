from django import forms
from .models import Patient
import re

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        if not re.match(r'^(98|97|96)\d{8}$', mobile):
            raise forms.ValidationError(
                "Mobile must be 10 digits and start with 98, 97 or 96"
            )
        return mobile