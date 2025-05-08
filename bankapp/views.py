from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Customer, Card, Type, Fellow
from .forms import DepositForm, WithdrawForm, CardSelectionForm

def frontpage(request):
    return render(request, 'frontpage.html', {})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        if Customer.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose a different username.")
            return render(request, 'signup.html', {'uname': username})
        try:
            customer = Customer(
                username=username,
                password=make_password(password),  # Hash the password
                balance=0.00
            )
            customer.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred during signup: {str(e)}")
            return render(request, 'signup.html', {'uname': username})
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        try:
            customer = Customer.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is None:
                from django.contrib.auth.models import User
                user, _ = User.objects.get_or_create(username=username)
                user.set_password(password)
                user.save()
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('customer_details')
        except Customer.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return render(request, 'login.html', {'uname': username})
        except Exception as e:
            messages.error(request, f"An error occurred during login: {str(e)}")
            return render(request, 'login.html', {'uname': username})
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def customer_details(request):
    if request.user.is_authenticated:
        customers = Customer.objects.filter(username=request.user.username)
        return render(request, 'customer_details.html', {'customers': customers})
    return redirect('login')

def deposit(request, id):
    customer = get_object_or_404(Customer, id=id, username=request.user.username)
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
    customer = get_object_or_404(Customer, id=id, username=request.user.username)
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