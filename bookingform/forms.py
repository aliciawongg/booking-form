from django import forms
from .models import customerBooking

class customerBookingForm(forms.ModelForm):
    class Meta:
        model = customerBooking
        fields = [
            'customer_name',
            'email',
            'contact_num',
            'date_time',
            'service'
        ]