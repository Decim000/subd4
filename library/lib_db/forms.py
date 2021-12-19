from django import forms
from django.forms import widgets

from .models import Reader, Order

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('book', 'reader', 'date_of_order')
        labels = {
            
            "book": "Номер книги",
            "reader": "Читатель",
            "date_of_order": "Дата возврата"
        }
        widgets = {
            "date_of_order": DateInput(),
        }

class ReaderForm(forms.ModelForm):
    
    class Meta:
        model = Reader
        fields = ('fio', 'phone')
        labels = {
            
            "fio": "ФИО читателя",
            "phone": "Телефон",
        }
       