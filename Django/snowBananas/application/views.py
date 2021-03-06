from django.shortcuts import render, redirect, HttpResponse
from . models import User, SnowBanana
import bcrypt
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
# RENDER METHODS
def dispLogin(request):
    uid = request.session.get('userID')
    if uid is not None:
        return redirect('/dashboard')
    else:
        return render(request, 'index.html')

def dispDashboard(request):
    # uid = request.session['myEmail']
    uid = request.session.get('userID')
    thisUser = User.objects.get(id=uid)
    if uid is not None:
        context = {
            'sbananas': SnowBanana.objects.all(),
            'myBananas':SnowBanana.objects.filter(user=thisUser),
            'thisUser': User.objects.get(id=uid)
        }
        return render(request, "dashboard.html", context)
    else:
        return redirect('/')

def dispGuest(request, name):
    context = {
        'theName': name,
        'theAge': 129
    }
    return render(request, 'guest.html', context)

def dispCreate(request):
    return render(request, 'create.html')


# ACTION METHODS
def login(request):
    # request.session['myEmail'] = request.POST['email']
    # request.session['prefName'] = request.POST['fName']
    existingUser = User.objects.filter(
        email = request.POST['email']
    ).first()
    if existingUser is not None:
        if bcrypt.checkpw(request.POST['pWord'].encode(), existingUser.password.encode()): # evaluates to either True or False
        # if existingUser.password == request.POST['pWord']:
            request.session['userID'] = existingUser.id
            return redirect('/dashboard')
        else:
            print('password does not match')
    else:
        print('user does not exist')
    return redirect('/')

def newUser(request):

    #adding some validations
    # if len(request.POST['fName'])<2:
    #     messages.error(request, 'First name must be at least 2 characters.')
    # if len(request.POST['lName'])<2:
    #     messages.error(request, 'Last name must be at least 2 characters.')

    # error_messages = messages.get_messages(request)
    # error_messages.used = False

    errors = User.objects.basic_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')

    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    print(hashed_pw)
    new_user = User.objects.create(
        first_name = request.POST['fName'],
        last_name = request.POST['lName'],
        email = request.POST['email'],
        password = hashed_pw

    )
    request.session['userID'] = new_user.id
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def createNewNanna(request):
    newNanna = SnowBanana.objects.create(
        color=request.POST['color'],
        ripeness=request.POST['ripeness'],
        age=request.POST['age'],
        user= User.objects.get(id=request.session['userID'])
    )
    return redirect('/dashboard')

def likeANanna(request, nannaID):
    bananaToLike = SnowBanana.objects.get(id=nannaID)
    thisUser = User.objects.get(id=request.session['userID'])
    bananaToLike.users_who_like.add(thisUser)
    print(f'you liked the banana with id = {nannaID}')
    return redirect('/dashboard')