from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField('Название задачи', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title