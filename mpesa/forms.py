from django import forms


class ExpressNumberForm(forms.Form):
    phone = forms.CharField(
        max_length=12,
        min_length=10,
        widget=forms.TextInput(attrs={'name': 'phone'}),
        label="Phone number",
        initial=254,
        help_text="your mpesa registerd phone number",
    )
    amount = forms.IntegerField()
