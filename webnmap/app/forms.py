from django import forms


class NewScanForm(forms.Form):
    schedule = [
        (False, 'Сразу'),
        (True, 'Как расписание')
    ]

    argument = [
        ('-sS', 'TCP SYN сканирование'),
        ('-sT', 'TCP сканирование с использованием системного вызова connect'),
        ('-sU', 'Различные типы UDP сканирования'),
        ('-sA', 'TCP ACK сканирование'),
        ('-sW', 'TCP Window сканирование'),
        ('-sM', 'TCP сканирование Мэймона (Maimon)'),
        ('-sO', 'Сканирование IP протокола')
    ]

    hostname = forms.CharField(label='Имя хоста', max_length=100,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    arguments = forms.CharField(label='Аргументы', max_length=100, required=False,
                               widget=forms.RadioSelect(choices=argument))
    add_schedule = forms.CharField(label='Стартовать сразу или добавить как расписание?',
                                   widget=forms.RadioSelect(choices=schedule))
