from django.db import models


class Scan(models.Model):
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Начато')
    finished_at = models.DateTimeField(auto_now=True, verbose_name='Окончено')
    status = models.CharField(max_length=20, default='В процессе', verbose_name='Статус')
    is_finished = models.BooleanField(default=False, verbose_name='Завершено?')
    hostname = models.CharField(max_length=150, verbose_name='Имя хоста')
    arguments = models.CharField(max_length=150, blank=True, verbose_name='Аргументы')
    report = models.TextField(blank=True, verbose_name='Отчет')

    def __str__(self):
        return f'{self.hostname} {self.arguments}'

    class Meta:
        verbose_name = "Сканирование"
        verbose_name_plural = "Сканирования"
        ordering = ['-started_at']
