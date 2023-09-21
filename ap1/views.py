import data as data
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from ap1.models import Customer
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FellowCreationForm
from .models import Fellow, Type


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
        if Customer.objects.filter(username=uname).count() > 0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = Customer.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

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


def deposit(request, id):
    customers = Customer.objects.get(id=id)
    template = loader.get_template('deposit.html')
    context = {
       'customers': customers,
        }
    return HttpResponse(template.render(context, request))


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


def withdraw(request, id):
    customers = Customer.objects.get(id=id)
    template = loader.get_template('withdraw.html')
    context = {
       'customers': customers,
        }
    return HttpResponse(template.render(context, request))


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
            return redirect('add')
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
























# By John Koshy
