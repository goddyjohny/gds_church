from decimal import Decimal
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.


def list_cash_accounts(request):
    template = 'cash_account/list.html'
    title = 'Cash Account'
    page_title = 'Cash Account'
    table_title = 'List Cash Account'

    accounts = CashAccount.objects.all()

    context = {
        'accounts': accounts,
        'title': title,
        'page_title': page_title,
        'table_title': table_title,

    }
    return render(request, template, context)


def ref_no(Object):
    # Object refer to class name
    data = datetime.now()
    # get first object
    obj = Object.objects.first()

    if obj:
        # object id + 1
        number = obj.id + 1
        objno = data.strftime("%Y%m%d")+f"{number}"
        return objno
    else:
        objno = data.strftime("%Y%m%d1")
        return objno


def list_contributions(request):
    template = 'contribution/list.html'
    page_title = 'Contributions'
    table_title = 'List Contributions'

    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.ref_no = ref_no(Contribution)
            contribution.save()

            messages.success(request, "Contribution is successfully Added")
            form = ContributionForm()
        else:
            print(form.errors)
    else:
        form = ContributionForm()

    contributions = Contribution.objects.all()

    context = {
        'contributions': contributions,
        'page_title': page_title,
        'table_title': table_title,
        'form': form,

    }
    return render(request, template, context)


def edit_contribution(request, *args, **kwargs):
    id = kwargs.get('id')
    contribution = Contribution.objects.filter(id=id).first()
    template = 'contribution/edit.html'
    page_title = 'Edit Contribution'
    title = 'Update Contribution'
    if request.method == 'POST':
        form = ContributionForm(request.POST, instance=contribution)
        if form.is_valid():
            form.save()
            messages.success(request, "Contribution is successfully Updated")
            return redirect('finance:list_contributions')
        else:
            print(form.errors)
    else:
        form = ContributionForm(instance=contribution)

    context = {
        'form': form,
        'page_title': page_title,
        'title': title,
    }
    return render(request, template, context)


def view_contribution(request, *args, **kwargs):
    id = kwargs.get('id')
    contribution = Contribution.objects.filter(id=id).first()
    template = 'contribution/view.html'
    page_title = 'Contribution Details'
    cash_form = CashContributionForm()
    pledge_form = PledgeForm()

    context = {
        'contribution': contribution,
        'page_title': page_title,
        'cash_form': cash_form,
        'pledge_form': pledge_form
    }
    return render(request, template, context)


def debit_cash_account(Object, amount, description: str):
    # Object is a content_object
    # Get first cash account object
    cash = CashAccount.objects.first()
    # Get last balance
    last_balance = cash.balance if cash else Decimal(0.0)
    new_balance = last_balance + Decimal(amount)

    CashAccount.objects.create(content_object=Object, ref_no=ref_no(
        CashAccount), description=description, debit=amount, balance=new_balance)


def credit_cash_account(Object, description: str):
    # Object is a content_object 
    # Get first cash account object
    cash = CashAccount.objects.first()
    # Get last balance
    last_balance = cash.balance if cash else Decimal(0.0)
    new_balance = last_balance - Decimal(Object.amount)

    CashAccount.objects.create(content_object=Object, ref_no=ref_no(
        CashAccount), description=description, credit=Object.amount, balance=new_balance)


def add_cash_contribution(request, *args, **kwargs):
    id = kwargs.get('id')
    contribution = Contribution.objects.filter(id=id).first()

    if request.method == 'POST':
        form = CashContributionForm(request.POST)
        if form.is_valid():
            cash = form.save(commit=False)
            cash.contribution = contribution
            cash.ref_no = ref_no(CashContribution)
            cash.received_by = Member.objects.first()
            cash.save()

            contribution.balance = contribution.balance + cash.amount
            contribution.save()
            debit_cash_account(
                Object=cash, amount=cash.amount, description="Cash contribution added")

            messages.success(
                request, "Cash contribution is successfully Added")
            return redirect('finance:view_contribution', contribution.id)
        else:
            print(form.errors)
    else:
        form = CashContributionForm()

    return redirect('finance:view_contribution', contribution.id)


def add_pledge(request, *args, **kwargs):
    id = kwargs.get('id')
    contribution = Contribution.objects.filter(id=id).first()

    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            pledge = form.save(commit=False)
            pledge.contribution = contribution
            pledge.save()
            messages.success(
                request, "Pledge is successfully Added")
            return redirect('finance:view_contribution', contribution.id)
        else:
            print(form.errors)
    else:
        form = PledgeForm()

    return redirect('finance:view_contribution', contribution.id)


def list_offering_divisions(request):
    template = 'division/list.html'
    page_title = 'Offering Divisions'
    table_title = 'List Offering Divisions'

    if request.method == 'POST':
        form = OfferingDivisionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Offering Division is successfully Added")
            form = OfferingDivisionForm()
        else:
            print(form.errors)
    else:
        form = OfferingDivisionForm()

    divisions = OfferingDivision.objects.all()

    context = {
        'divisions': divisions,
        'page_title': page_title,
        'table_title': table_title,
        'form': form,

    }
    return render(request, template, context)


def activate_offering_divisions(request, *args, **kwargs):
    id = kwargs.get('id')
    division = OfferingDivision.objects.filter(id=id).first()
    OfferingDivision.objects.exclude(
        id=id).all().update(active=False)
    division.active = True
    division.save()
    return redirect('finance:list_offering_divisions')
       

def offering_division(amount,percent):
    new_amount= (amount*percent)/100
    return new_amount
    

def list_offerings(request):
    template = 'offering/list.html'
    page_title = 'Offerings'
    table_title = 'List Offerings'
    # Get active offering division
    division = OfferingDivision.objects.filter(active=True).first()

    if request.method == 'POST':
        form = OfferingForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.ref_no = ref_no(OfferingDivision)
            offer.kigango = offering_division(amount=offer.amount,percent= division.kigango)
            offer.parish = offering_division(
                amount=offer.amount, percent=division.parish)
            offer.diocese = offering_division(
                amount=offer.amount, percent=division.diocese)
            offer.division=division
            offer.save()
            
            debit_cash_account(Object=offer, amount=offer.kigango, description="Offering added")
            messages.success(
                request, "Offering is successfully Added")
            form = OfferingForm()
        else:
            print(form.errors)
    else:
        form = OfferingForm()

    offerings = Offering.objects.all()

    context = {
        'offerings': offerings,
        'page_title': page_title,
        'table_title': table_title,
        'form': form,
    }
    return render(request, template, context)
