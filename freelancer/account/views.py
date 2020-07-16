from django.shortcuts import render, redirect
from django.contrib import messages
# from django.http import JsonResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, 'account.html', {'company_name': 'Freelancer'})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if(password != password2):
            messages.error(request, 'Passwords do not match.')
            return redirect('/account/')
            # return JsonResponse({
            #     'success': False,
            #     'message': 'Passwords do not match',
            # }, json_dumps_params={'indent': 2})
        elif(User.objects.filter(username=username).exists()):
            messages.error(request, 'Username already taken.')
            return redirect('/account/')
        elif(User.objects.filter(email=email).exists()):
            messages.error(request, 'Email already taken.')
            return redirect('/account/')
        else:
            user = User(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(request, 'User account created. Please log in.')
            return redirect('/account/')
            # return JsonResponse({
            #     'success': True,
            #     'message': 'New user created',
            # }, json_dumps_params={'indent': 2})

    return redirect('/account/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials.')

    return redirect('/account/')

def logout(request):
    auth.logout(request)
    return redirect('/')