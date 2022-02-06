from django import forms
from rooms import models as room_models


class SearchForm(forms.Form):

    name = forms.CharField(required=False, label="상품명")
    nation = forms.ModelChoiceField(
        required=False, queryset=room_models.Nation.objects.all(), label="국가"
    )
    brand = forms.ModelChoiceField(
        required=False, queryset=room_models.Brand.objects.all(), label="브랜드"
    )
    category = forms.ModelChoiceField(
        required=False, queryset=room_models.Category.objects.all(), label="카테고리"
    )
    delivery_from = forms.ModelChoiceField(
        required=False, queryset=room_models.DeliveryFrom.objects.all(), label="배송조건"
    )
    delivery_term = forms.ModelChoiceField(
        required=False, queryset=room_models.DeliveryTerm.objects.all(), label="배송기간"
    )
    """
    colors = forms.ModelMultipleChoiceField(
        required=False,
        queryset=room_models.ItemColor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    """
