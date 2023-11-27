from django import forms
from .models import Items

class productForm(forms.ModelForm):
      class Meta:
            model=Items
            fields=['name','image','category','subcategory','reorder_level','cost_price','selling_price']