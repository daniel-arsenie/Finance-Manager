from django.db import models

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
    paid_with = models.ForeignKey(BankAccount, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=18)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.date_time}....{self.category}..{self.paid_with}..' \
               f'{self.location}..{self.description}..{self.amount}'
