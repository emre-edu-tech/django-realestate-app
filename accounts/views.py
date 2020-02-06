from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        # check for user registration
        # messages.error(request, 'Testing error message')
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            # check if username already exists
            # we imported the User model above
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
                # check if email already exists
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already being used')
                return redirect('register')
            else:
                # info looks good go ahead and create the user
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                # Login after user registration
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                # register the user then redirect to index page for them to login
                user.save()
                messages.success(request, 'You are now registered can log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # check for user login
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid user credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    data = {
        'user_contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', data)
