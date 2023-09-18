# import data as data
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from bankapp.models import Customer
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .forms import FellowCreationForm
from .models import Fellow, Type

from django.shortcuts import render, redirect
from .models import Customer
from .forms import DepositForm, WithdrawForm

def frontpage(request):
    return render(request, 'frontpage.html', {})

# Create your views here.
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        customers = Customer.objects.filter(username=current_user).values()

        param = {'customers': customers, 'current_user': current_user}

        return render(request, 'customer_details.html', param)
    else:
        return redirect('login')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        
        # Check if username already exists
        if Customer.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken. Please choose a different username.")
            return render(request, 'signup.html', {'uname': uname})
        
        # Create a new Customer (not User)
        try:
            customer = Customer(
                username=uname,
                password=make_password(pwd),  # Hash the password
                balance=0.00,   # Set default balance
            )
            customer.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred during signup: {str(e)}")
            return render(request, 'signup.html', {'uname': uname})

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        try:
            customer = Customer.objects.get(username=uname)
            if check_password(pwd, customer.password):  # Check hashed password
                request.session['user'] = uname
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.error(request, "Invalid password.")
                return render(request, 'login.html', {'uname': uname})
        except Customer.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return render(request, 'login.html', {'uname': uname})

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')


def customer_details(request):
    if 'user' in request.session:
        current_user = request.session['user']
        customers = Customer.objects.filter(username=current_user).values()
        template = loader.get_template('customer_details.html')
        context = {
            'customers': customers
            }
        return HttpResponse(template.render(context, request))


def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount <= 0:
                form.add_error('amount', 'Amount must be positive.')
                return render(request, 'deposit.html', {'form': form})
            customer = Customer.objects.get(user=request.user)
            customer.balance += amount
            customer.deposit = amount
            customer.save()
            return redirect('customer_details')
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form})


def deposit_amount(request, id):
    dep = request.POST['dep_cash']
    customers = Customer.objects.get(id=id)
    customers.deposit = dep
    bal = int(customers.balance)
    d = int(dep)
    bal += d
    customers.balance = bal
    customers.save()
    return HttpResponseRedirect(reverse('customer_details'))


def withdraw(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            customer = Customer.objects.get(user=request.user)
            if amount <= 0:
                form.add_error('amount', 'Amount must be positive.')
                return render(request, 'withdraw.html', {'form': form})
            if amount > customer.balance:
                form.add_error('amount', 'Insufficient balance.')
                return render(request, 'withdraw.html', {'form': form})
            customer.balance -= amount
            customer.withdrawal = amount
            customer.save()
            return redirect('customer_details')
    else:
        form = WithdrawForm()
    return render(request, 'withdraw.html', {'form': form})


def withdraw_amount(request, id):
    wit = request.POST['wit_cash']
    customers = Customer.objects.get(id=id)
    customers.withdrawal = wit
    bal = int(customers.balance)
    w = int(wit)
    bal -= w
    customers.balance = bal
    customers.save()
    return HttpResponseRedirect(reverse('customer_details'))


def card_selection(request):
    form = FellowCreationForm()
    if request.method == 'POST':
        form = FellowCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    return render(request, 'home.html', {'form': form})


def update_view(request, pk):
    fellow = get_object_or_404(Fellow, pk=pk)
    form = FellowCreationForm(instance=fellow)
    if request.method == 'POST':
        form = FellowCreationForm(request.POST, instance=fellow)
        if form.is_valid():
            form.save()
            return redirect('change', pk=pk)
    return render(request, 'home.html', {'form': form})


def load_types(request):
    card_id = request.GET.get('card_id')
    types = Type.objects.filter(card_id=card_id).all()
    return render(request, 'type_dropdown_list_options.html', {'types': types})


def success(request):
    return render(request, 'confirmation.html')





















# By John Koshy
