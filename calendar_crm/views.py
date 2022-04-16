from django.shortcuts import render, redirect
from accounts.models import *
# Create your views here.


def calendar(request, username):
    if request.user.username !=username:
        return redirect('error', username)
    else:
        user = User.objects.get(username=username)
        if request.user.username !=username:
            return redirect('error', username)
        elif Employe.objects.filter(user=user):
            user = User.objects.get(username=username)
            employe = Employe.objects.get(user=user)
            position1 = Postion.objects.get(id=employe.position.id)
    context = {
        'position1':position1,
    }
    return render(request,'calendar.html', context)