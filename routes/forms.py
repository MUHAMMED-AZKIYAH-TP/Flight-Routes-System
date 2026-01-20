from django import forms
from .models import AirportRoute, Airport


class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = "__all__"


class NthNodeForm(forms.Form):
    root = forms.ModelChoiceField(queryset=Airport.objects.all())
    direction = forms.ChoiceField(choices=[("left", "Left"), ("right", "Right")])
    n = forms.IntegerField(min_value=1)
    
class LongestRouteForm(forms.Form):
    airport = forms.ModelChoiceField(queryset=Airport.objects.all())
    
    
class ShortestRouteForm(forms.Form):
    airport = forms.ModelChoiceField(queryset=Airport.objects.all())


