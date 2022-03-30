from owner.models import Mobile
from django import forms


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"
        widgets = {
            "model_name":forms.TextInput(attrs={"class":"form-control"}),
            "brand": forms.TextInput(attrs={"class":"form-control"}),
            "price": forms.NumberInput(attrs={"class":"form-control"}),
            "color": forms.TextInput(attrs={"class":"form-control"}),
            "available_stock":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
         }