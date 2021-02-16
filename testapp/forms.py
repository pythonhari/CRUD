from django import forms

class Employeeform(forms.Form):
    eno = forms.IntegerField()
    ename = forms.CharField(max_length=100)
    esal = forms.FloatField()
    eaddr = forms.CharField(max_length=100)
    ephno = forms.IntegerField()


class Updateform(forms.Form):
    eno=forms.IntegerField()
    esal=forms.FloatField()
class Deleteform(forms.Form):
    eno=forms.IntegerField()