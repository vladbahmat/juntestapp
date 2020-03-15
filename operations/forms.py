from django import forms
 
class SortForm(forms.Form):
    CH_LIST=[('Buble','Buble'),('Merge','Merge'),('Inserts','Inserts')]
    name = forms.CharField(max_length=20,choices=CH_LIST,default='Buble')
    upload = forms.IntegerField()