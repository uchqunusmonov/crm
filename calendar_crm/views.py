from django.http import JsonResponse
from django.shortcuts import render, redirect
from accounts.models import *
from tasks.models import *
from datetime import date, timedelta



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
    all_events = Task.objects.all()
    d = date(2020, 1, 1)
    d += timedelta(days=6 - d.weekday()) # First Sunday
    all_sunday_in_2020 = []
    while d.year != 2021:
        all_sunday_in_2020.append({'name': 'my-title', 'start': d, 'end': d 
        + timedelta(days=1)})
        d += timedelta(days=7)
        return render(request,'calendar.html',{'events':all_sunday_in_2020})
    context = {
        'position1':position1,
        "events":all_events,
    }
    return render(request,'calendar.html', context)

        


def all_events(request):                                                                                                 
    all_events = Task.objects.filter(active=True)
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                     
    return JsonResponse(out, safe=False)  

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Task(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Task.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Task.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)