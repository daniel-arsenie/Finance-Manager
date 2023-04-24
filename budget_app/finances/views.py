from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Spending
from .forms import SpendingForm
from .filters import SpendingFilter


def pie_chart(request):

    qs = Spending.objects.values('category__name').annotate(total_amount=Sum('amount')).order_by('category__name')

    labels = [d['category__name'] for d in qs]
    data = [d['total_amount'] for d in qs]

    return render(request, 'finances/pie_chart.html', {
        'labels': labels,
        'data': data,
    })


# class ExpenseStructureView(TemplateView):
#     template_name = 'finances/pie_chart.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         qs = Spending.objects.values('category').annotate(total_amount=Sum('amount'))
#         context["categories"] = [d['category'] for d in qs]
#         context["totals"] = [d['total_amount'] for d in qs]
#         return context


def delete_spending(request, id):
    post = get_object_or_404(Spending, id=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'finances/confirm_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        return redirect('finances:all-spendings')


def edit_spending(request, id):
    post = get_object_or_404(Spending, id=id)

    if request.method == 'GET':
        context = {'form': SpendingForm(instance=post), 'id': id}
        return render(request, 'finances/add_spending.html', context)
    elif request.method == 'POST':
        form = SpendingForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('finances:all-spendings')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'finances/add_spending.html', {'form': form})


def add_spending(request):
    submitted = False
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_spending?submitted=True')
    else:
        form = SpendingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'finances/add_spending.html', {'form': form, 'submitted': submitted})


# Create your views here.
def all_spendings(request):
    spending_filter = SpendingFilter(request.GET, queryset=Spending.objects.all().order_by('-date_time'))
    context = {
        'form': spending_filter.form,
        'spendings_list': spending_filter.qs
    }

    return render(request, 'finances/spending_list.html', context)


def index(request):
    total_income = Spending.objects.filter(record_type='income').aggregate(Sum('amount'))
    total_expenses = Spending.objects.filter(record_type='expense').aggregate(Sum('amount'))
    if total_income['amount__sum'] is None:
        total_income['amount__sum'] = 0
        budget_left = total_income['amount__sum'] - total_expenses['amount__sum']
        return render(request, 'finances/homepage.html', {'budget_left': budget_left,
                                                          'total_expenses': total_expenses,
                                                          'total_income': total_income,
                                                          })
    budget_left = total_income['amount__sum'] - total_expenses['amount__sum']

    return render(request, 'finances/homepage.html', {'budget_left': budget_left,
                                                      'total_expenses': total_expenses,
                                                      'total_income': total_income,
                                                      })
