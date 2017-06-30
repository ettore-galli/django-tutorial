from django import forms



class CalcForm(forms.Form):
     x = forms.FloatField()
     y = forms.FloatField()
 