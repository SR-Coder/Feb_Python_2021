from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# RENDER METHODS
def dispLogin(request):
    return render(request, 'index.html')

def dispDashboard(request):
    context = {
        'nameList': ['Kelly', 'Billy', 'Brenda']
    }
    return render(request, "dashboard.html", context)

def dispGuest(request, name):
    context = {
        'theName': name,
        'theAge': 129
    }
    return render(request, 'guest.html', context)


# ACTION METHODS
def createNew(request):
    myName = request.POST['fName']
    myEmail = request.POST['email']
    return redirect('/dashboard')

