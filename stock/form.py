from django import forms

class TickerForm(forms.Form):
    ticker=forms.CharField(label='Ticker',max_length=5)

def clean(self):
    user = self.authenticate_via_email()
    if not user:
        raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
    else:
        self.user = user
    return self.cleaned_data
