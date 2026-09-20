from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        label='Restaurant Name',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Enter restaurant name',

        }))
    url=forms.URLField (label='Menu URL',
                        max_length=200,
                        widget=forms.URLInput(attrs={'class': 'form-control',
                        'placeholder': 'Enter menu URL',}))