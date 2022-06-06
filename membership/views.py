from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.


def list_dioceses(request):
    dioceses = Diocese.objects.all()
    
    context ={
        'dioceses': dioceses,
    }
    return render(request, 'list_dioceses.html',context)


def add_diocese(request):
    if request.method=='POST':
        form = DioceseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership:list_dioceses')
        else:
            print(form.errors)    
    else:
        form = DioceseForm()

    context = {
        'form': form,
    }
    return render(request, 'add_diocese.html', context)


def edit_diocese(request, *args, **kwargs):
    id = kwargs.get('id')
    diocese = Diocese.objects.filter(id=id).first()

    if request.method == 'POST':
        form = DioceseForm(request.POST, instance=diocese)
        if form.is_valid():
            form.save()
            return redirect('membership:list_dioceses')
        else:
            print(form.errors)
    else:
        form = DioceseForm(instance=diocese)

    context = {
        'form': form,
    }
    return render(request, 'edit_diocese.html', context)


def list_deacons(request):
    deacons = Deacon.objects.all()

    context = {
        'deacons': deacons,
    }
    return render(request, 'list_deacons.html', context)


def add_deacon(request):
    if request.method == 'POST':
        form = DeaconForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership:list_deacons')
        else:
            print(form.errors)
    else:
        form = DeaconForm()

    context = {
        'form': form,
    }
    return render(request, 'add_deacon.html', context)


def edit_deacon(request, *args, **kwargs):
    id = kwargs.get('id')
    deacon = Deacon.objects.filter(id=id).first()

    if request.method == 'POST':
        form = DeaconForm(request.POST, instance=deacon)
        if form.is_valid():
            form.save()
            return redirect('membership:list_deacons')
        else:
            print(form.errors)
    else:
        form = DeaconForm(instance=deacon)

    context = {
        'form': form,
    }
    return render(request, 'edit_deacon.html', context)


def list_parishes(request):
    parishes = Parish.objects.all()

    context = {
        'parishes': parishes,
    }
    return render(request, 'list_parishes.html', context)


def add_parish(request):
    if request.method == 'POST':
        form = ParishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership:list_parishes')
        else:
            print(form.errors)
    else:
        form = ParishForm()

    context = {
        'form': form,

    }
    return render(request, 'add_parish.html', context)


def edit_parish(request, *args, **kwargs):
    id = kwargs.get('id')
    parish = Parish.objects.filter(id=id).first()

    if request.method == 'POST':
        form = ParishForm(request.POST, instance=parish)
        if form.is_valid():
            form.save()
            return redirect('membership:list_parishes')
        else:
            print(form.errors)
    else:
        form = ParishForm(instance=parish)

    context = {
        'form': form,

    }
    return render(request, 'edit_parish.html', context)
