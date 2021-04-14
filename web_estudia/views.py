from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = 'Name: ' + name + ' Email: ' + email + ' Message: ' + request.POST['message']

        #send an Email
        send_mail(
            name,
            message,
            email,
            ['sahilrohilla03@gmail.com', 'cernasayuri@gmail.com'],
            )
        return render(request, 'web_estudia/index.html', {'name': name})

    else:
        return render(request, 'web_estudia/index.html', {})
