from django import forms


class NewScanForm(forms.Form):
    host = forms.CharField(label='Хост или хосты для сканирования', max_length=100)
    arguments = form.CharField(label='', max_length=100)