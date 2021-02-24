from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

#############################################
# Login and REG METHODS
# Create your views here.
def dispLogin(request):
    return render(request, 'login.html')

def dipsSuccess(request):
    # isNotLoggedIn(request)
    if 'userID' not in request.session:
        return redirect('/')

    return render(request, 'success.html')

#Action methods
def register(request):
    #when i click register i come here and i determine what
    # get post data from from
        # this comes in on request.POST
    # validate that everything valid
    errors = User.objects.register_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        # if invalid we return redirect to the register page
        return redirect('/')
        
    # if valid add to database and login bcrypt 
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        first_name=request.POST['fName'],
        last_name=request.POST['lName'],
        email=request.POST['email'],
        password=pw_hash
    )
    request.session['userID'] = newUser.id
    return redirect('/success')

def login(request):
    #this is for when you click the loging button
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        # if invalid we return redirect to the register page
        return redirect('/')
    user = User.objects.get(email=request.POST['email']) 
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['userID'] = user.id
        return redirect('/success')
    else:
        messages.error(request, "email or password invalid")
        return redirect('/')

def logout(request):
    #this is for logging out
    request.session.clear()
    return redirect('/')


#############################################
# HELPER FUNCTIONS
def isNotLoggedIn(request):
    print('in helper function')
    if "userID" not in request.session:
        return redirect('/')
#############################################
# Make your belt exam stuff here
