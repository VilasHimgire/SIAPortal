from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.
def index(request):
    # return HttpResponse("hello Everyone")
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'html/assignment.html')

def loginUser(request):
    if request.method == "POST":
        usern = request.POST['username']
        userp = request.POST['password']
        user = authenticate(request,username=usern,password=userp)
        print(usern,end="\n")
        print(userp)
        if user is not None:
            login(request,user)
            return redirect('/')
    else:
        return render(request,'html/login.html')
    return render(request,'html/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')


def notes(request):
    return render(request, 'html/notes.html')

def assignment(request):
    return render(request, 'html/assignment.html')

# def register(request):
#     return render(request, 'html/register.html')

from .forms import StudentForm

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = StudentForm()
    return render(request, 'html/register.html', {'form': form})
