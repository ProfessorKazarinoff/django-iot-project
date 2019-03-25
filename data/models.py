# data/models.py

from django.db import models

# Create your models here.

class Data(models.Model):
    DATA_TYPE_CHOICES = (('flt', "Float"), ('str', "string"))
    created_at = models.DateTimeField(auto_now_add=True)
    channel_num = models.PositiveSmallIntegerField()
    field_num = models.PositiveSmallIntegerField()
    data_flt = models.DecimalField(max_digits=19, decimal_places=10)
    data_str = models.CharField(max_length=20)
    uploaded_by = models.CharField(max_length=30)
    data_pt_num = models.PositiveIntegerField()
    data_pt_type = models.CharField(max_length=3, choices=DATA_TYPE_CHOICES, default='flt')

    def __str__(self):
        return f'{self.created_at} channel: {self.channel_num} field: {self.field_num} data: {self.data_flt}'
