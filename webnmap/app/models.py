from django.db import models


class Scan(models.Model):
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Начато')
    finished_at = models.DateTimeField(auto_now=True, verbose_name='Окончено')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name='Статус')
    is_finished = models.BooleanField(default=False, verbose_name='Завершено?')
    hostname = models.ForeignKey('Hostname', on_delete=models.PROTECT, verbose_name='Имя хоста')
    arguments = models.ForeignKey('Arguments', on_delete=models.PROTECT, verbose_name='Аргументы')
    report = models.TextField(blank=True, verbose_name='Отчет')

    def __str__(self):
        return f'{self.hostname} {self.arguments}'

    class Meta:
        verbose_name = "Сканирование"
        verbose_name_plural = "Сканирования"
        ordering = ['-started_at']


class Hostname(models.Model):
    hostname = models.CharField(max_length=100, verbose_name='Имя хоста', primary_key=True)

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = "Имя хоста"
        verbose_name_plural = "Имена хоста"
        ordering = ['hostname']


class Arguments(models.Model):
    arguments = models.CharField(max_length=150, default='-', verbose_name='Аргументы', primary_key=True)

    def __str__(self):
        return self.arguments

    class Meta:
        verbose_name = "Аргументы"
        verbose_name_plural = "Аргументы"
        ordering = ['arguments']


class Status(models.Model):
    status = models.CharField(max_length=20, default='В процессе', verbose_name='Статус', primary_key=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ['status']


class Schedule(models.Model):
    start_date = models.DateTimeField(verbose_name='Дата и время начала')
    interval = models.IntegerField(verbose_name='Интервал')
    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    hostname = models.ForeignKey('Hostname', on_delete=models.PROTECT)
    arguments = models.ForeignKey('Arguments', on_delete=models.PROTECT)
    # last triggered at datetime

    def __str__(self):
        return f'{self.hostname} {self.arguments}'

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        ordering = ['hostname']
