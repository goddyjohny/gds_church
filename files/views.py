from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import *
from .models import *
# Create your views here.

@login_required(login_url='accounts:login')
def upload_file(request):
    template = 'add.html'
    title = 'Add File'
    table_title = 'List Of Files'

    document = Document.objects.filter(Q(user=request.user)|Q(shared_users=request.user))  

    # instanciate a form

    form = DocumentForm(request.POST or None, request.FILES)

    #Check the validity of the form
    if request.method == 'POST':

        if form.is_valid():
            file_obj = form.save(commit=False)
            file_obj.user=request.user
            file_obj.save()
            messages.success(request,"Successfully file uploaded")
            return redirect('files:files-upload')
    else:
        form = DocumentForm()

     
     
    context = {
        'title':title,
        'table_title':table_title,
        'form':form,
        'document':document
    }

    return render(request, template, context)

# @login_required(login_url='accounts:login')
# def update_file(request,id):
#     template = 'add.html'
#     title = 'Update File'
#     table_title = 'List Of Files'

#     document = Document.objects.filter(Q(user=request.user)|Q(shared_users=request.user))  

#     #obtain the object to be edited

#     doc_id =get_object_or_404(Document,pk=id)

    

#     #Instantiniate the form

#     form = DocumentForm(request.POST or None,instance=doc_id)

#     if request.method == 'POST':
#         if form.is_valid():
#             file_obj = form.save(commit=False)
#             file_obj.save()
#             messages.success(request,"Successfully file updated")
#             return redirect('files:files-upload')

#     else:
#         form = DocumentForm(instance=doc_id)

#     context = {
#         'title':title,
#         'table_title':table_title,
#         'form':form,
#         'document':document
#     }

#     return render(request, template, context)



        
        
