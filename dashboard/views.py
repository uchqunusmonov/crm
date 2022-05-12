from django.shortcuts import redirect, render
from accounts.models import User, Employe
from accounts.models import Postion, AdduserCount
from django.contrib.auth.decorators import login_required

from tasks.models import Task
# Create your views here.

@login_required(login_url='user_login')
def dashboard(request, username):
    if request.user.username !=username:
        return redirect('error', username)
    else:
        user = User.objects.get(username=username)
        employe = Employe.objects.get(user=user)
        
        position1 = Postion.objects.get(id=employe.position.id)
        user_count = User.objects.all().count()
        employes = Employe.objects.all()
        users = User.objects.all()
        task_count = Task.objects.filter(employe=employe)
        employe_country = {}
        for el in Employe.COUNTRY:
            employe_country[el[0]] = Employe.get_country(el[0])
        for i in AdduserCount.objects.all():
            procent = (user_count*100)/i.users            
    context = {
        'user':user,
        'employe':employe,
        'procent':procent,
        'position1':position1,
        'user_count':user_count,
        'employes':employes,
        'users':users,
        'task_count':task_count,
        'employe_country':list(employe_country.values()),
    }
    return render(request, 'dashboard.html', context)
