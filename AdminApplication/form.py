
from django import forms
from AdminApplication.models import StateModel
from AdminApplication.models import CityModel
from AdminApplication.models import AreaModel

class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = ('state_name',)

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = "__all__"
        exclude = ('city_no',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = "__all__"
        exclude = ('area_no',)