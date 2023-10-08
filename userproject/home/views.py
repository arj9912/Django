from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import logout ,authenticate,login
# password for  test user is Arjun$$$***000
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
         return redirect("/login")
         
    return render(request, 'index.html')

def loginUser(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        user = request.POST.get('password')
        print(username)


        user = authenticate(username="username", password="password")

    if user is not None:
    # A backend authenticated the credentials
        login(request, user)
        return redirect("/")
    else:
    # No backend authenticated the credentials
         return redirect(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")