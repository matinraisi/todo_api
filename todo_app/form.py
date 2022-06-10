from django import forms
from .models import category,todo_list

class Datainput(forms.DateInput):
    input_type = 'date'


class todo_listForm(forms.ModelForm):
    created = forms.DateField(widget=Datainput)
    class Meta:
        model = todo_list
        fields = ('title', 'created','category')