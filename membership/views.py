from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Kanda,Kigango
from .forms import KandaForm, KigangoForm

# Create your views here.


def add_kigango(request):
    template = 'demography/kigango/add.html'
    title = 'Add Kigango'
    table_title = 'List Of Kigango'

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
        'kigango':kigango
    }    

    return render(request, template, context)




def update_kigango(request,id):

    template = 'demography/kigango/add.html'
    title = 'Add Kigango'
    table_title = 'List Of Kigango'

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
        'kigango':kigango
    }    

    return render(request, template, context)





def add_kanda(request):
    template = 'demography/kanda/add.html'
    title = 'Add Kanda'
    table_title = 'List Of Kanda'

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
        'kanda':kanda
    }    

    return render(request, template, context)




def update_kanda(request,id):

    template = 'demography/kanda/add.html'
    title = 'Add Kanda'
    table_title = 'List Of Kanda'

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
        'kanda':kanda
    }    

    return render(request, template, context)




    

