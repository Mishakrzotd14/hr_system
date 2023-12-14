from django.db import models
from datetime import datetime


HIERARCHY_CHOICES = (
    (0, 'Генеральный директор'),
    (1, 'Руководитель высшего звена'),
    (2, 'Менеджер среднего звена'),
    (3, 'Руководитель отдела'),
    (4, 'Обычный сотрудник'),
)


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_employment = models.DateField(default=datetime.now, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_info = models.CharField(max_length=100)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    hierarchy_level = models.IntegerField(choices=HIERARCHY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.full_name