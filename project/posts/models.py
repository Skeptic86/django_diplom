from django.db import models

# Create your models here.
class Posts(models.Model):
    theme = models.CharField('Тема', max_length=30)
    date = models.DateField('Дата и время')
    is_shkn = models.BooleanField('Шкн в названии')
    is_link = models.BooleanField('Есть ссылка')
    appointment = models.CharField('Назначение', max_length=50)

    def __str__(self):
        return f'{self.theme}:{self.appointment}'
    
    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

    