from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
from django.shortcuts import redirect, render
from django.contrib.auth.forms import authenticate
from accounts.models import User, Employe
from accounts.models import Postion
# Create your views here.


def dashboard(request, username):

    if request.user.username !=username:
         return redirect('error', username)
    else:
        user = User.objects.get(username=username)
        employe = Employe.objects.get(user=user)
        position = Postion.objects.filter(id=employe.position.id)
        user_count = User.objects.all().count()
        s = 22
        procent = (user_count*100)/s
    context = {
        'user':user,
        'employe':employe,
        'procent':procent,
        'position':position
    }


    return render(request, 'dashboard.html', context)
=======


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')
>>>>>>> 7f2061c7ab5ff73ea00efc0c281c5298dd14c277
