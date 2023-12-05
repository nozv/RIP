from django.db import models


# Create your models here.
class Service(models.Model):
    class Meta:
        verbose_name = ' услугу'
        verbose_name_plural = 'Услуги'
    service_name = models.CharField(max_length=100, verbose_name='Наименование услуги')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость')
    image = models.TextField(verbose_name='Изображение', null=True)
    description = models.TextField(verbose_name='Описание', null=True)
    last_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')


class Appointment(models.Model):
    phone = models.CharField(max_length=12, verbose_name='Телефон')

class Doctor(models.Model):
    class Meta:
        verbose_name = ' врача'
        verbose_name_plural = 'Врачи'
    doc_name = models.CharField(max_length=60, verbose_name='ФИО')
    doc_spec = models.CharField(max_length=60, verbose_name='Специальность', default=None)

    def __str__(self):
        return self.doc_name

days = ((1,'ПН'), (2,'ВТ'), (3,'СР'), (4,'ЧТ'), (5,'ПТ'), (6,'СБ'))


class Schedule(models.Model):
    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'Расписание'
        unique_together = ('doc', 'day')
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    day = models.PositiveSmallIntegerField(verbose_name='День недели', choices=days)
    sch = models.TextField(verbose_name='Расписание', null=True)


    def display_doc_name(self):
        return self.doc.doc_name
    display_doc_name.short_description = 'ФИО'

    def display_doc_spec(self):
        return self.doc.doc_spec
    display_doc_spec.short_description = 'Специальность'

