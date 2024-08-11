from django.shortcuts import render


# Create your views here.
def registration(request):
    if request.method == 'POST':
        data = request.POST
        user_name = data.get('userName')
        user_email = data.get('userEmail/')
        phone_number = data.get('phone')
        gender = data.get('userGender')
        

    context={'page_title' : 'Registration Page',}
    return render(request, "registration.html", context)

def login(request):
    context={'page_title':'Registration Page',}
    return render(request, "login.html", context)