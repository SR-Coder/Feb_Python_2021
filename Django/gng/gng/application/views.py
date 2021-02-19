from django.shortcuts import render, redirect
import random

# Create your views here.
# DISPLAY ROUTE
def index(request):
    theRandom = request.session.get('savedRandom')
    if theRandom is None:
        request.session['savedRandom'] = random.randint(1,100)
        request.session['gameStatus'] = 3
        print(f'from the if ---> {request.session["savedRandom"]}')
        return render(request, 'index.html')
    else:
        print(f'from the else ---> {request.session["savedRandom"]}')
        return render(request, 'index.html')


# ACTION ROUTE
def makeGuess(request):
    if request.POST['theGuess']!= "":
        thisGuess = int(request.POST['theGuess'])
        theRandom = request.session['savedRandom']
        if thisGuess == theRandom:
            request.session['gameStatus'] = 0
            print('winner winner chicken dinner!!')
        elif thisGuess > theRandom:
            request.session['gameStatus'] = 1
            print('too high')
        elif thisGuess < theRandom:
            request.session['gameStatus'] = 2
            print('too low')
        else:
            request.session['gameStatus'] = 3
            print('use a number dummy!!')
        return redirect('/')
    else:
        return redirect('/')

def resetGame(request):
    request.session.clear()
    return redirect('/')
   
   
   
   
 # print(f'This Guess = {thisGuess}, and the Number is {request.session["savedRandom"]}')