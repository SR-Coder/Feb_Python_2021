from django.shortcuts import render, redirect, HttpResponse
from . models import User

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
    if uid is not None:
        context = {
            'nameList': ['Kelly', 'Billy', 'Brenda']
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


# ACTION METHODS
def login(request):
    # request.session['myEmail'] = request.POST['email']
    # request.session['prefName'] = request.POST['fName']
    existingUser = User.objects.filter(
        email = request.POST['email']
    ).first()
    if existingUser is not None:
        if existingUser.password == request.POST['pWord']:
            request.session['userID'] = existingUser.id
            return redirect('/dashboard')
        else:
            print('password does not match')
    else:
        print('user does not exist')
    return redirect('/')

def logout(request):
    del request.session['myEmail']
    request.session.clear()
    return redirect('/')

