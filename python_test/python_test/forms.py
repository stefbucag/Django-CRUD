from django import forms
from models import Client
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ClientForm(forms.ModelForm):
    """Form for add client."""

    class Meta:
        """Meta."""

        model = Client
        fields = (
            'name',
            'email',
            'phone',
            'postcode',
            'state',
            'street',
            'suburb',
        )


class AddClientForm(forms.ModelForm):
    """Actual saving of the client."""

    email = forms.EmailField(required=True)

    class Meta:
        """Meta."""

        model = Client
        fields = (
            'name',
            'email',
            'phone',
            'postcode',
            'state',
            'street',
            'suburb',
        )

    def save(self, commit=True):
        """Save client."""
        client = super(AddClientForm, self).save(commit=False)
        client.name = self.cleaned_data['name']
        client.email = self.cleaned_data['email']

        if commit:
            client.save()

        return client


class EditClientForm(forms.ModelForm):
    """Edit client information form."""

    class Meta:
        """Meta."""

        model = Client
        fields = (
            'name',
            'email',
            'phone',
            'postcode',
            'state',
            'street',
            'suburb',
        )
