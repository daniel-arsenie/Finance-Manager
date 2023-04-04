from django.urls import path
from . import views

app_name = 'finances'

urlpatterns = [
    path('', views.index, name='index'),
    path('spendings/', views.all_spendings, name='all-spendings'),
    path('add_spending/', views.add_spending, name='add-spending'),
    path('edit_spending/<int:id>', views.edit_spending, name='edit-spending'),
    path('delete_spending/<int:id>', views.delete_spending, name='delete-spending'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),

]
