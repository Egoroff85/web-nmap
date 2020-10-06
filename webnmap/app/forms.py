from django import forms


class NewScanForm(forms.Form):
    SCHEDULE = [
        (False, 'Сразу'),
        (True, 'Как расписание')
    ]

    ARGUMENT = [
        ('-sS', 'TCP SYN сканирование'),
        ('-sT', 'TCP сканирование с использованием системного вызова connect'),
        ('-sU', 'Различные типы UDP сканирования'),
        ('-sA', 'TCP ACK сканирование'),
        ('-sW', 'TCP Window сканирование'),
        ('-sM', 'TCP сканирование Мэймона (Maimon)'),
        ('-sO', 'Сканирование IP протокола')
    ]

    INTERVALS = [
        (1, '1 час'),
        (2, '2 часа'),
        (4, '4 часа'),
        (8, '8 часов')
    ]

    hostname = forms.CharField(label='Имя хоста', max_length=100,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    arguments = forms.CharField(label='Аргументы', max_length=100, widget=forms.RadioSelect(choices=ARGUMENT),
                                initial='-sS')
    add_schedule = forms.BooleanField(label='Стартовать сразу или добавить как расписание?',
                                      widget=forms.RadioSelect(choices=SCHEDULE), initial=False)
    interval = forms.IntegerField(label='Интервал расписания в часах', required=False,
                                  widget=forms.RadioSelect(choices=INTERVALS), initial=1)
