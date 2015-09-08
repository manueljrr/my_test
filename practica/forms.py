__author__ = 'Manuel'

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Producto

class ProductoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))
        super(ProductoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Producto
