from django.contrib import admin
from .models import Category, BankAccount, Spending
# Register your models here.

admin.site.register(BankAccount)
admin.site.register(Category)
admin.site.register(Spending)
