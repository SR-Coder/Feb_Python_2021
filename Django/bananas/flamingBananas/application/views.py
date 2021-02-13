from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#DISPLAY METHODS

def displayIndex(request):
    return HttpResponse('hello world')

def helloAge(request, myAge ):
    return HttpResponse(f'hello my age is {myAge}')

def displayPayments(request):
    return render(request, 'index.html')

def displaySuccess(request):
    return render(request, 'success.html')

#ACTION METHODS
def sendHome(request):
    return redirect('/')

def processCard(request):
    #action
    print('this is the backend charging your card!!!!')
    return redirect('/success')