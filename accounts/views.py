from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.



# login view:

def userlogin(request):
    """checking the http method if is a post method"""
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    
    if request.method == 'POST':
        """Getting data from template by post method"""
        username = request.POST['username']
        password = request.POST['password']

        """authenticate the received credentials if are valid"""
        user = authenticate(request, username=username, password=password)

        """Checking if user is existing and is staff"""
        if user is not None:
            # if user.is_staff:
                """allow user to login and redirect to dashboard"""
                login(request, user)
                return redirect('dashboard:index')
            # else:
            #     """if user is not staff"""
            #     messages.error(request, 'Sorry Only Staff can get access')
            #     return redirect('accounts:login')

        else:

            """notifying a user who is not a Staff that has got no permission to login"""
            messages.error(request, 'Credentials are invalid')
            return redirect('accounts:login')
    return render(request, 'login.html')


# logout view
@login_required(login_url='accounts:login')
def userlogout(request):
    """Taking a librarian out of the dashboard """
    logout(request)
    return redirect('accounts:login')

