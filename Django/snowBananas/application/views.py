from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# RENDER METHODS
def dispLogin(request):
    uid = request.session.get('myEmail')
    if uid is not None:
        return redirect('/dashboard')
    else:
        return render(request, 'index.html')

def dispDashboard(request):
    # uid = request.session['myEmail']
    uid = request.session.get('myEmail')
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
def createNew(request):
    request.session['myEmail'] = request.POST['email']
    request.session['prefName'] = request.POST['fName']
    return redirect('/dashboard')

def logout(request):
    del request.session['myEmail']
    request.session.clear()
    return redirect('/')

