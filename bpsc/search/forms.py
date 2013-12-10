from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField
from gmapi.forms.widgets import GoogleMap

class ResourcePrintForm(forms.Form):
    # We set the 'queryset' field in __init__. This is passed from the view
    client_name = forms.CharField(label="Client's Name")
    client_phone = USPhoneNumberField(label="Client's Phone (Optional)", required=False)
    client_email = forms.EmailField(label="Client's Email (Optional)", required=False)
    user_email = forms.EmailField(label="Your Email")

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':500, 'height':500}))