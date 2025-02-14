from django import forms
from .models import Reservation, GalleryImage

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone_number', 'number_of_people', 'date', 'time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders and classes to form fields
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Your Name',
            'class': 'form-control bg-transparent border-0 px-3',
        })
        self.fields['phone_number'].widget.attrs.update({
            'placeholder': 'Phone Number',
            'class': 'form-control bg-transparent border-0 px-3',
        })
        self.fields['number_of_people'].widget.attrs.update({
            'placeholder': 'Number of People',
            'class': 'form-control bg-transparent border-0 px-3',
        })
        self.fields['date'].widget.attrs.update({
            'type': 'date',
            'class': 'form-control bg-transparent border-0 px-3',
        })
        self.fields['time'].widget.attrs.update({
            'type': 'time',
            'class': 'form-control bg-transparent border-0 px-3',
        })

    def clean_date(self):
        return self.cleaned_data['date']

    def clean_time(self):
        return self.cleaned_data['time']
    

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'css_class']    