from django.shortcuts import render,redirect,get_object_or_404
from decimal import Decimal
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.




@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
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



@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
def activate_offering_divisions(request, *args, **kwargs):
    id = kwargs.get('id')
    division = OfferingDivision.objects.filter(id=id).first()
    OfferingDivision.objects.exclude(
        id=id).all().update(active=False)
    division.active = True
    division.save()
    return redirect('finance:list_offering_divisions')
       
@login_required(login_url='accounts:login')
def offering_division(amount,percent):
    new_amount= (amount*percent)/100
    return new_amount
    
@login_required(login_url='accounts:login')
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


@login_required(login_url='accounts:login')
def  expense_category(request):
    template = 'expense/listcategory.html'
    title = 'Add Category'
    table_title = 'List Of Categories'
    page_title='Finance'

    category = ExpenseCategory.objects.all()

    #Instantiate the form

    form = ExpenseCategoryForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            cat_obj = form.save(commit=False)
            cat_obj.save()
            messages.success(request,"Category Created Successfully")
            return redirect('finance:category')
        else:
            
            messages.error(request,form.errors)    
    else:
        form = ExpenseCategoryForm()

    context = {
        'form':form,
        'title':title,
        'category':category,
        'table_title':table_title,
        'page_title':page_title
    }            

    return render(request, template, context)


@login_required(login_url='accounts:login')
def expense_category_updates(request, id):
    template = 'expense/edit.html'
    title = 'Update Category'
    table_title = 'List Of Categories'
    page_title='Finance'

    category = ExpenseCategory.objects.all()

    cat_id = get_object_or_404(ExpenseCategory,pk=id)

    

    #Instantiate the form
    form = ExpenseCategoryForm(request.POST or None, instance=cat_id)

    if request.method == 'POST':
        if form.is_valid():
            cat_obj = form.save(commit=False)
            cat_obj.save()
            messages.success(request,"Category Updated Successfully")
            return redirect('finance:category')
        else:
            
            messages.error(request,form.errors)    
    else:
        form = ExpenseCategoryForm(instance=cat_id)

    context = {
        'form':form,
        'title':title,
        'category':category,
        'table_title':table_title,
        'page_title':page_title
    }            

    return render(request, template, context)    




@login_required(login_url='accounts:login')
def expense_categoryname(request):
    template = 'expense/listname.html'
    title = 'Add Expense Name'
    table_title = 'List Of Expense Name'
    page_title='Finance'

    name = ExpenseName.objects.all()

    #Instantiate the form

    form = ExpenseNameForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name_obj = form.save(commit=False)
            name_obj.user=request.user
            name_obj.save()
            messages.success(request,"Expense Name Created Successfully")
            return redirect('finance:expense-name')
        else:
            
            messages.error(request,form.errors)    
    else:
        form = ExpenseNameForm()

    context = {
        'form':form,
        'title':title,
        'name':name,
        'table_title':table_title,
        'page_title':page_title
    }            

    return render(request, template, context)



@login_required(login_url='accounts:login')
def update_expense_categoryname(request, id):
    template = 'expense/edit.html'
    title = 'Update Expense Name'
    table_title = 'List Of Expense Name'
    page_title='Finance'

    name = ExpenseName.objects.all()

    name_id = get_object_or_404(ExpenseName,pk=id)

    

    #Instantiate the form
    form = ExpenseNameForm(request.POST or None, instance=name_id)

    if request.method == 'POST':
        if form.is_valid():
            name_obj = form.save(commit=False)
            name_obj.save()
            messages.success(request,"Expense Name Updated Successfully")
            return redirect('finance:expense-name')
        else:
            
            messages.error(request,form.errors)    
    else:
        form = ExpenseNameForm(instance=name_id)

    context = {
        'form':form,
        'title':title,
        'name':name,
        'table_title':table_title,
        'page_title':page_title
    }

    return render(request, template, context)       





@login_required(login_url='accounts:login')
def expense(request):
    template = 'expense/listexpense.html'
    title = 'Add Expense'
    table_title = 'List Of Expenses'
    page_title='Finance'

    expense = Expense.objects.all()

    #Instantiate the form

    form = ExpenseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            expense_obj = form.save(commit=False)
            expense_obj.save()
            messages.success(request,"Expense Recorded Successfully")
            return redirect('finance:expense')
        else:
            
            messages.error(request,form.errors)    
    else:
        form = ExpenseForm()

    context = {
        'form':form,
        'title':title,
        'expense':expense,
        'table_title':table_title,
        'page_title':page_title
    }            

    return render(request, template, context)



@login_required(login_url='accounts:login')
def update_expense(request, id):
    template = 'expense/edit.html'
    title = 'Update Expense'
    table_title = 'List Of Expense'
    page_title='Finance'

    expense = Expense.objects.all()
  
    expense_id = get_object_or_404(Expense,pk=id)

    #Instantiate the form
    form = ExpenseForm(request.POST or None, instance=expense_id)

    if request.method == 'POST':
        if form.is_valid():
           
            expense_obj = form.save(commit=False)       
            expense_obj.save()
            messages.success(request,"Expense  Updated Successfully")
            return redirect('finance:expense')       
    else:
        form = ExpenseForm(instance=expense_id)

    context = {
        'form':form,
        'title':title,
        'expense':expense,
        'table_title':table_title,
        'page_title':page_title
    }

    return render(request, template, context)    



@login_required(login_url='accounts:login')
def property(request):
    template = 'deposit/listprop.html'
    title = 'Add Property'
    table_title = 'List Of Properties'
    page_title='Finance'

    properties = Property.objects.all()

    #Instantiate the form

    form = PropertyForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.save()
            messages.success(request,"Property Recorded Successfully")
            return redirect('finance:property')
        else:
            
            messages.error(request,form.errors)    
    else:
        form = PropertyForm()

    context = {
        'form':form,
        'title':title,
        'property':properties,
        'table_title':table_title,
        'page_title':page_title
    }            

    return render(request, template, context)


@login_required(login_url='accounts:login')
def update_property(request, id):
    template = 'deposit/edit.html'
    title = 'Update Property'
    table_title = 'List Of Properties'
    page_title='Finance'

    properties = Property.objects.all()
  
    property_id = get_object_or_404(Property,pk=id)

    #Instantiate the form
    form = PropertyForm(request.POST or None, instance=property_id)

    if request.method == 'POST':
        if form.is_valid():
           
            property_obj = form.save(commit=False)       
            property_obj.save()
            messages.success(request,"Property  Updated Successfully")
            return redirect('finance:property')       
    else:
        form = PropertyForm(instance=property_id)

    context = {
        'form':form,
        'title':title,
        'property':properties,
        'table_title':table_title,
        'page_title':page_title
    }

    return render(request, template, context)     



@login_required(login_url='accounts:login')
def deposit(request):
    template = 'deposit/depositlist.html'
    title = 'Add Deposit'
    table_title = 'List Of Deposit'
    page_title='Finance'

    deposit = Deposit.objects.all()

    #Instantiate the form

    form = DepositForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            deposit_obj = form.save(commit=False)
            deposit_obj.depositor = request.user
            deposit_obj.save()
            messages.success(request,"Deposit Recorded Successfully")
            return redirect('finance:deposit')
        else:
            
            messages.error(request,form.errors)    
    else:
        form = DepositForm()

    context = {
        'form':form,
        'title':title,
        'deposit':deposit,
        'table_title':table_title,
        'page_title':page_title
    }            

    return render(request, template, context)     


@login_required(login_url='accounts:login')
def update_deposit(request, id):
    template = 'deposit/edit.html'
    title = 'Update Deposit'
    table_title = 'List Of Deposit'
    page_title='Finance'

    deposit = Deposit.objects.all()
  
    deposit_id = get_object_or_404(Deposit,pk=id)

    #Instantiate the form
    form = DepositForm(request.POST or None, instance=deposit_id)

    if request.method == 'POST':
        if form.is_valid():
           
            deposit_obj = form.save(commit=False)       
            deposit_obj.save()
            messages.success(request,"Deposit  Updated Successfully")
            return redirect('finance:deposit')       
    else:
        form = DepositForm(instance=deposit_id)

    context = {
        'form':form,
        'title':title,
        'deposit':deposit,
        'table_title':table_title,
        'page_title':page_title
    }

    return render(request, template, context)  
   

@login_required(login_url='accounts:login')
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


@login_required(login_url='accounts:login')
def debit_cash_account(Object, amount, description: str):
    # Object is a content_object
    # Get first cash account object
    cash = CashAccount.objects.first()
    # Get last balance
    last_balance = cash.balance if cash else Decimal(0.0)
    new_balance = last_balance + Decimal(amount)

    CashAccount.objects.create(content_object=Object, ref_no=ref_no(
        CashAccount), description=description, debit=amount, balance=new_balance)


@login_required(login_url='accounts:login')
def credit_cash_account(Object, description: str):
    # Object is a content_object 
    # Get first cash account object
    cash = CashAccount.objects.first()
    # Get last balance
    last_balance = cash.balance if cash else Decimal(0.0)
    new_balance = last_balance - Decimal(Object.amount)

    CashAccount.objects.create(content_object=Object, ref_no=ref_no(
        CashAccount), description=description, credit=Object.amount, balance=new_balance)            



@login_required(login_url='accounts:login')
def expense_debit(request, id):
    
    debit = get_object_or_404(Expense,pk=id)
    credit_cash_account(
                Object=debit, amount=debit.amount, description="Cash Expense withdrawn")
    debit.is_debited = True
    debit.save()
    messages.success(request,"The amount "+ str(debit.amount) +" is successfully debited from the Account")
    return redirect('finance:expense')


    # if balance.balance > 0:
    #     if debit.is_debited == False:

    #         if balance.balance >= debit.amount:
    #             balance.balance = balance.balance - debit.amount
    #             balance.save()
    #             debit.is_debited = True
    #             debit.save()
    #             messages.success(request,"The amount "+ str(debit.amount) +" is successfully debited from the Account")
    #             return redirect('finance:expense')
    #         else:  
    #             messages.error(request,"Excuse the account balance is insufficient to debit "+ str(debit.amount))  
    #             return redirect('finance:expense')
    #     else:
    #         messages.error(request,"This amount already debited")
    #         return redirect('finance:expense')

    # else:
    #     messages.error(request,"Excuse the account balance is "+str(balance.balance))  
    #     return redirect('finance:expense')


@login_required(login_url='accounts:login')
def deposit_credit(request, id):
   
    credit = get_object_or_404(Deposit,pk=id)
    debit_cash_account(Object=credit, amount=credit.amount, description="Cash added")
    credit.is_credited = True   
    credit.save()   
    messages.success(request,"The amount "+ str(credit.amount) +" is successfully credited to the Account")
    return redirect('finance:deposit')      

    # if balance.balance >= 0:
    #     if credit.is_credited == False:

    #         balance.balance = balance.balance + credit.amount
    #         balance.save()
    #         credit.is_credited = True
    #         credit.save()
    #         messages.success(request,"The amount "+ str(credit.amount) +" is successfully credited to the Account")
    #         return redirect('finance:deposit')
    #     else:
    #         messages.error(request,"This amount already credited")
    #         return redirect('finance:deposit')

 
    # else:
    #     messages.error(request,"Something Wrong ") 
    #     return redirect('finance:deposit')



    

        


