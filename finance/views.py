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
    debit_cash_account(
                Object=credit, amount=credit.amount, description="Cash added")
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



    

         





    