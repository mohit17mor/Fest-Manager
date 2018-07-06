from django.shortcuts import render, redirect
from .forms import LoginForm, CreateContractForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Contract
from datetime import datetime

def home_page(request):
    context={}
    return render(request,'home_page.html',context)

def login_view(request):
    form = LoginForm()
    context = {
        'form' : form,
    }
    return render(request, 'login.html', context)

def auth(request):
    form = LoginForm(request.POST)
    if(request.method == "POST"):
        if(form.is_valid):
            u_type = form['type_of_user'].value()
            username = form['username'].value()
            password = form['password'].value()

            user = authenticate(username = username, password = password)

            if user and user.get_type() == u_type:
                login(request, user)
                return redirect('/dashboard/')
            else:
                return redirect('/login/')
    else:
        return HttpResponse('/auth/')

@login_required(login_url='/login')
def dashboard(request):
    user = User.objects.get(id=request.session['_auth_user_id'])
    if user.user_type == 1:     # organiser type
        ps_user = User.objects.get(username = 'pseudo')
        available_contracts = Contract.objects.filter(organiser = ps_user)
        current_contracts = Contract.objects.filter(organiser = user)

        proshow_contracts = available_contracts.filter(contract_type = 'proshow')
        catering_contracts = available_contracts.filter(contract_type = 'catering')
        logistics_contracts = available_contracts.filter(contract_type = 'logistics')

        cart_total = 0
        for contr in current_contracts:
            cart_total += contr.price

        context = {
            'current_contracts': current_contracts,
            # 'available_contracts': available_contracts,
            'proshow_contracts': proshow_contracts,
            'catering_contracts': catering_contracts,
            'logistics_contracts': logistics_contracts,
            'cart_total': cart_total,
        }
        return render(request, 'organiser_dashboard.html', context)

    elif user.user_type == 2: # vendor type
        ps_user = User.objects.get(username = 'pseudo')
        taken_contracts = Contract.objects.filter(vendor = user).exclude(organiser = ps_user)
        not_taken=Contract.objects.filter(vendor = user).filter(organiser = ps_user)
        context = {
            'taken_contracts': taken_contracts,
            'not_taken':not_taken,
        }
        return render(request, 'vendor_dashboard.html', context)

# def add_contract(request, id):
#     contr = Contract.objects.get(pk = id)
#     user = User.objects.get(id=request.session['_auth_user_id'])
#     contr.organiser = user
#     contr.save()
#     return HttpResponse('hello')

def cart(request):
    user = User.objects.get(id=request.session['_auth_user_id'])
    if user.user_type == 1:     # organiser type
        current_contracts = Contract.objects.filter(organiser = user)
        cart_total = 0
        for contr in current_contracts:
            cart_total += contr.price

        context = {
            'current_contracts': current_contracts,
            'cart_total': cart_total,
        }
        return render(request, 'cart.html', context)

    elif user.user_type == 2:
        return HttpResponse('Cart feature not available for vendors')

def add_to_cart(request, id):
    user = User.objects.get(id=request.session['_auth_user_id'])
    contr = Contract.objects.get(pk = id)
    contr.organiser = user
    contr.date_of_contract = datetime.now().date()
    contr.save()
    return redirect('/dashboard/')

def logout_view(request):
    logout(request)
    return redirect('/home/')

def create_contract(request):
    if request.method == 'GET':
        form = CreateContractForm()
        context = {
            'form': form,
        }
        return render(request, 'create_contract.html', context)
    elif request.method == 'POST':
        user = User.objects.get(id=request.session['_auth_user_id'])
        ps_user = User.objects.get(username = 'pseudo')
        form = CreateContractForm(request.POST)
        contr = form.save(commit=False)
        contr.vendor = user
        contr.organiser = ps_user
        contr.save()
        return redirect('/dashboard/')

def add_package1(request):
    user = User.objects.get(id=request.session['_auth_user_id'])

    contracts = []
    contracts.append(Contract.objects.get(id = 35))
    contracts.append(Contract.objects.get(id = 31))
    contracts.append(Contract.objects.get(id = 26))
    for contr in contracts:
        contr.organiser = user
        contr.date_of_contract = datetime.now().date()
        contr.save()
    return redirect('/dashboard/')

def add_package2(request):
    user = User.objects.get(id=request.session['_auth_user_id'])

    contracts = []
    contracts.append(Contract.objects.get(id = 36))
    contracts.append(Contract.objects.get(id = 29))
    contracts.append(Contract.objects.get(id = 42))
    for contr in contracts:
        contr.organiser = user
        contr.date_of_contract = datetime.now().date()
        contr.save()
    return redirect('/dashboard/')

def add_package3(request):
    user = User.objects.get(id=request.session['_auth_user_id'])

    contracts = []
    contracts.append(Contract.objects.get(id = 37))
    contracts.append(Contract.objects.get(id = 34))
    contracts.append(Contract.objects.get(id = 44))
    for contr in contracts:
        contr.organiser = user
        contr.date_of_contract = datetime.now().date()
        contr.save()
    return redirect('/dashboard/')

def remove_contract(request, id):
    contract = Contract.objects.get(pk = id)
    contract.delete()
    return redirect('/dashboard/')

def edit_contract(request, id):
    contract = Contract.objects.get(pk = id)
    if request.method=='GET':
        values = {
            'vendor': contract.vendor,
            'organiser': contract.organiser,
            'description': contract.description,
            'date_of_contract': contract.date_of_contract,
            'price': contract.price,
            'contract_type': contract.contract_type,
        }

        form = CreateContractForm(initial = values)
        context = {
            'form': form,
            'contrid': id,
        }
        return render(request, 'contract_edit.html', context)
    elif request.method == 'POST':
        form = CreateContractForm(request.POST)
        contract.description = form['description'].value()
        contract.price = form['price'].value()
        contract.contract_type = form['contract_type'].value()
        contract.save()
        return redirect('/dashboard/')

def remove_from_cart(request, id):
    contract = Contract.objects.get(pk = id)
    ps_user = User.objects.get(username = 'pseudo')
    contract.organiser = ps_user
    contract.save()
    return redirect('/cart/')
