from django.db import models


class Scan(models.Model):
    STATUSES = [
        ('В процессе', 'В процессе'),
        ('Ошибка', 'Ошибка'),
        ('Завершено', 'Завершено')
    ]

    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Начато')
    finished_at = models.DateTimeField(auto_now=True, verbose_name='Окончено')
    is_finished = models.BooleanField(default=False, verbose_name='Завершено?')
    status = models.CharField(
        max_length=100,
        choices=STATUSES,
        default='В процессе',
        verbose_name='Статус'
    )
    hostname = models.ForeignKey('Hostname', on_delete=models.PROTECT, verbose_name='Имя хоста')
    arguments = models.ForeignKey('Arguments', on_delete=models.PROTECT, verbose_name='Аргументы')
    report = models.JSONField(null=True, verbose_name='Отчет')
    celery_task_id = models.CharField(max_length=100, null=True, verbose_name='Идентификатор задачи Celery')

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
    arguments = models.CharField(max_length=100, verbose_name='Аргументы', primary_key=True)

    def __str__(self):
        return self.arguments

    class Meta:
        verbose_name = "Аргументы"
        verbose_name_plural = "Аргументы"
        ordering = ['arguments']


class Schedule(models.Model):
    hostname = models.ForeignKey('Hostname', on_delete=models.PROTECT)
    arguments = models.ForeignKey('Arguments', on_delete=models.PROTECT)
    interval = models.IntegerField(verbose_name='Интервал в часах')
    is_active = models.BooleanField(default=True, verbose_name="Активно?")

    def __str__(self):
        return f'{self.hostname} {self.arguments}'

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        ordering = ['hostname']
