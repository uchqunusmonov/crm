from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def email_send(request):
    if request.method == "POST":
        message_author = request.POST['message-author']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
        
        #send an email
        
        send_mail(
            message_author,
            message_email,
            message_text,
            ['']
        )
        
    return render(request, 'email.html')
        