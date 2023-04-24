from datetime import datetime

from _decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


RECORD_TYPE = [
    ('expense', 'Expense'),
    ('income', 'Income'),
]


class Category(models.Model):
    name = models.CharField('Category Name', max_length=30)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    name = models.CharField('Bank Account Name', max_length=15)

    def __str__(self):
        return self.name


class Spending(models.Model):
    record_type = models.CharField(max_length=7, choices=RECORD_TYPE, default='other')
    paid_with = models.ForeignKey(BankAccount, blank=True, null=True, verbose_name='Card', on_delete=models.CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(Decimal('0.01'))])
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=25,
                                validators=[RegexValidator('[+-/%@!(){}]', inverse_match=True)]
                                )
    description = models.TextField(max_length=300, blank=True,
                                   validators=[RegexValidator('[+-/%@!()"{}]', inverse_match=True)]
                                   )

    def __str__(self):
        return f'{self.date_time}....{self.category}..{self.paid_with}..' \
               f'{self.location}..{self.description}..{self.amount}'
