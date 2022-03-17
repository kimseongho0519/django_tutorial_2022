from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import CountryData

class CountryDataForm(ModelForm):
    class Meta:
        model = CountryData
        # fields = ['country']  특정한 필드에서 사용할 때
        fields = '__all__'