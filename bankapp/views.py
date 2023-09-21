from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Card, Type
from .forms import DepositForm, WithdrawForm, CardSelectionForm

def frontpage(request):
    return render(request, 'frontpage.html', {})

def deposit(request, id):
    customer = get_object_or_404(Customer, id=id, user=request.user)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount <= 0:
                form.add_error('amount', 'Amount must be positive.')
                return render(request, 'deposit.html', {'form': form, 'customer': customer})
            customer.balance += amount
            customer.deposit = amount
            customer.save()
            return redirect('customer_details')
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form, 'customer': customer})

def withdraw(request, id):
    customer = get_object_or_404(Customer, id=id, user=request.user)
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount <= 0:
                form.add_error('amount', 'Amount must be positive.')
                return render(request, 'withdraw.html', {'form': form, 'customer': customer})
            if amount > customer.balance:
                form.add_error('amount', 'Insufficient balance.')
                return render(request, 'withdraw.html', {'form': form, 'customer': customer})
            customer.balance -= amount
            customer.withdrawal = amount
            customer.save()
            return redirect('customer_details')
    else:
        form = WithdrawForm()
    return render(request, 'withdraw.html', {'form': form, 'customer': customer})

def card_selection(request):
    if request.method == 'POST':
        form = CardSelectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CardSelectionForm()
    return render(request, 'home.html', {'form': form})

def update_view(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardSelectionForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CardSelectionForm(instance=card)
    return render(request, 'home.html', {'form': form})

def load_types(request):
    card_id = request.GET.get('card_id')
    types = Type.objects.filter(card_id=card_id).order_by('name')
    return render(request, 'type_dropdown_list_options.html', {'types': types})

def success(request):
    return render(request, 'success.html', {})

def phone_activation(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        # Add phone activation logic here (e.g., save to database or send SMS)
        return redirect('success')
    return render(request, 'base.html')