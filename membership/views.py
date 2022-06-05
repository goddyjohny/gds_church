from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Kanda,Kigango, Fellowship, Family, Member
from .forms import KandaForm, KigangoForm, FellowshipForm, FamilyForm, MemberForm


# Create your views here.


#Kigango

def add_kigango(request):
    template = 'demography/kigango/add.html'
    title = 'Add Kigango'
    table_title = 'List Of Kigango'
    page_title = 'Kigango'

    # register form and path request post

    form = KigangoForm(request.POST or None)

    #Check if the form is valid

    if form.is_valid():
        # creating model objbectb for saving

        kigango_obj = form.save(commit=False)

        #save to DB
        kigango_obj.save()
        messages.success(request, "Kigango is Added successfully")
        return redirect('add-kigango')

    # list all kanda
    kigango = Kigango.objects.all()

    context = {
        'form':form,
        'title':title,
        'table_title':table_title,
        'kigango':kigango,
        'page_title':page_title
    }    

    return render(request, template, context)




def update_kigango(request,id):

    template = 'demography/kigango/add.html'
    title = 'Add Kigango'
    table_title = 'List Of Kigango'
    page_title = 'Kigango'

    # get the object to be edited

    kigango_id = get_object_or_404(Kigango,pk=id)

    # set the editable one to form
    form = KigangoForm(request.POST or None, instance=kigango_id)

    if form.is_valid():
        # creating model objbect  for saving

        kigango_obj = form.save(commit=False)

        #save to DB
        kigango_obj.save()
        messages.success(request, "Kigango is Updated successfully")
        return redirect('add-kigango')

    # list all kanda
    kigango = Kigango.objects.all()

    context = {
        'form':form,
        'title':title,
        'table_title':table_title,
        'kigango':kigango,
        'page_title':page_title
    }    

    return render(request, template, context)



# Kanda

def add_kanda(request):
    template = 'demography/kanda/add.html'
    title = 'Add Kanda'
    table_title = 'List Of Kanda'
    page_title = 'Kanda'

    # register form and path request post

    form = KandaForm(request.POST or None)

    #Check if the form is valid

    if form.is_valid():
        # creating model objbectb for saving

        kanda_obj = form.save(commit=False)

        #save to DB
        kanda_obj.save()
        messages.success(request, "Kanda is Added successfully")
        return redirect('add-kanda')

    # list all kanda
    kanda = Kanda.objects.all()

    context = {
        'form':form,
        'title':title,
        'table_title':table_title,
        'kanda':kanda,
        'page_title':page_title
    }    

    return render(request, template, context)




def update_kanda(request,id):

    template = 'demography/kanda/add.html'
    title = 'Add Kanda'
    table_title = 'List Of Kanda'
    page_title = 'Kanda'

    # get the object to be edited

    kanda_id = get_object_or_404(Kanda,pk=id)

    # set the editable one to form
    form = KandaForm(request.POST or None, instance=kanda_id)

    if form.is_valid():
        # creating model objbectb for saving

        kanda_obj = form.save(commit=False)

        #save to DB
        kanda_obj.save()
        messages.success(request, "Kanda is Updated successfully")
        return redirect('add-kanda')

    # list all kanda
    kanda = Kanda.objects.all()

    context = {
        'form':form,
        'title':title,
        'table_title':table_title,
        'kanda':kanda,
        'page_title':page_title
        
    }    

    return render(request, template, context)



# Fellowship

def add_fellowship(request):
    template = 'demography/fellowship/add.html'
    title = 'Add Fellowship'
    table_title = 'List Of Fellowship'
    page_title = 'Jumuiya'

    # register form and path request post

    form = FellowshipForm(request.POST or None)

    #Check if the form is valid

    if form.is_valid():
        # creating model objbect for saving

        fellowship_obj = form.save(commit=False)

        #save to DB
        fellowship_obj.save()
        messages.success(request, "Fellowship is Added successfully")
        return redirect('add-fellowship')

    # list all kanda
    fellowship = Fellowship.objects.all()

    context = {
        'form':form,
        'title':title,
        'table_title':table_title,
        'fellowship':fellowship,
        'page_title':page_title
    }    

    return render(request, template, context)




def update_fellowship(request,id):

    template = 'demography/fellowship/add.html'
    title = 'Add Fellowship'
    table_title = 'List Of Fellowship'
    page_title = 'Jumuiya'

    # get the object to be edited

    fellowship_id = get_object_or_404(Fellowship,pk=id)

    # set the editable one to form
    form = FellowshipForm(request.POST or None, instance=fellowship_id)

    if form.is_valid():
        # creating model objbectb for saving

        fellowship_obj = form.save(commit=False)

        #save to DB
        fellowship_obj.save()
        messages.success(request, "Fellowship is Updated successfully")
        return redirect('add-fellowship')

    # list all kanda
    fellowship = Fellowship.objects.all()

    context = {
        'form':form,
        'title':title,
        'table_title':table_title,
        'fellowship':fellowship,
        'page_title':page_title
    }    

    return render(request, template, context)







    # Femily

def add_family(request):
    template = 'demography/family/add.html'
    title = 'Add Family'
    page_title = 'Familia'

    # register form and path request post

    form = FamilyForm(request.POST or None)

    #Check if the form is valid

    if form.is_valid():
        # creating model objbect for saving

        family_obj = form.save(commit=False)

        #save to DB
        family_obj.save()
        messages.success(request, "Family is Added successfully")
        return redirect('list-family')

    context = {
        'form':form,
        'title':title,
        'page_title':page_title
    }    

    return render(request, template, context)




def update_family(request,id):

    template = 'demography/family/add.html'
    title = 'Add Family'
    page_title = 'Familia'

    # get the object to be edited

    family_id = get_object_or_404(Family,pk=id)

    # set the editable one to form
    form = FamilyForm(request.POST or None, instance=family_id)

    if form.is_valid():
        # creating model objbectb for saving

        family_obj = form.save(commit=False)

        #save to DB
        family_obj.save()
        messages.success(request, "Family is Updated successfully")
        return redirect('list-family')


    context = {
        'form':form,
        'title':title,
        'page_title':page_title
    }    

    return render(request, template, context)


def list_family(request):
    template = 'demography/family/list.html'
    table_title = 'List Of Family'
    page_title = 'Familia'

    #return all family from DB

    family = Family.objects.all()

    context = {
        'table_title':table_title,
        'page_title':page_title,
        'family':family
    }    

    return render(request, template, context)





# Members

def add_member(request):
    template = 'demography/member/add.html'
    title = 'Taarifa za Muumini'
    page_title = 'Waumini'

    # register form

    form = MemberForm(request.POST or None)

    #Check if the form is valid
    if form.is_valid():

        #create object for the model

        member_obj = form.save(commit=False)

        #Save Data to DB

        member_obj.save()

        messages.success(request, "Member is Added Successfully")
       

    context = {
        'title':title,
        'page_title':page_title,
        'form':form
    } 
    
    return render(request, template, context)



def update_member(request,id):
    template = 'demography/member/add.html'
    title = 'Taarifa za Muumini'
    page_title = 'Waumini'

    # get the specific object to be edited

    member_id = get_object_or_404(Member,pk=id)

    # return object data to form for edit

    form = MemberForm(request.POST or None, instance=member_id)


    # Check the validity of the form

    if form.is_valid():

        # create object for saving data to DB
        member_obj = form.save(commit=False)
      
        # Save the object to DB
        member_obj.save()
        messages.success(request, "Member is successfully Updated")
        return redirect('list-member')

    context = {
        'title':title,
        'page_title':page_title,
        'form':form
    } 
    
    return render(request, template, context)    



def member_details(request,id):
    template = 'demography/member/view.html'
    page_title = 'Taarifa za Muumini'

    # get the details of particular member

    member_id = get_object_or_404(Member,pk=id)

    context = {
        'page_title':page_title,
        'member_id':member_id
    } 

    return render(request, template, context)




def list_member(request):
    template = 'demography/member/list.html'
    table_title = 'List Of Members'
    page_title = 'Waumini'

    member = Member.objects.all()

    context = {
        'table_title':table_title,
        'page_title':page_title,
        'member':member
    } 

    return render(request, template, context)


    










    

