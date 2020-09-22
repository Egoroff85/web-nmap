from django import forms


class NewScanForm(forms.Form):
    hostname = forms.CharField(label='Имя хоста', max_length=100,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    arguments = forms.CharField(label='Аргументы', max_length=100, required=False,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    add_schedule = forms.BooleanField(label='Добавить как расписание?', required=False, initial=False)