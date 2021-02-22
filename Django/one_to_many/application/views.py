from django.shortcuts import render, redirect
from .models import User, SnowBanana

# Create your views here.
def index(request):
    context = {
        'all_users' : User.objects.all()
    }
    return render(request, "index.html", context)

def dispCreate(request):
    context = {
        'userList':User.objects.all()
    }
    return render(request, 'create.html', context)



def createUser(request):
    chkUser = User.objects.filter(email=request.POST['email']).first()
    if chkUser is not None:
        return redirect('/create')
    else:
        newUser = User.objects.create(
            fname=request.POST['fName'],
            lname=request.POST['lName'],
            hair_color=request.POST['hair_color'],
            email=request.POST['email']
        )
        return redirect('/')

def createNanna(request):
    
    return redirect('/')