from django import forms
from rooms import models as room_models


class SearchForm(forms.Form):

    name = forms.CharField(required=False)
    nation = forms.ModelChoiceField(
        required=False, queryset=room_models.Nation.objects.all()
    )
    brand = forms.ModelChoiceField(
        required=False, queryset=room_models.Brand.objects.all()
    )
    category = forms.ModelChoiceField(
        required=False, queryset=room_models.Category.objects.all()
    )
    delivery_from = forms.ModelChoiceField(
        required=False, queryset=room_models.DeliveryFrom.objects.all()
    )
    delivery_term = forms.ModelChoiceField(
        required=False, queryset=room_models.DeliveryTerm.objects.all()
    )
    """
    colors = forms.ModelMultipleChoiceField(
        required=False,
        queryset=room_models.ItemColor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    """
