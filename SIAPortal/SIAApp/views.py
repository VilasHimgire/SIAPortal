from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .models import Student
from .models import Question
from .models import AssignmentResponse
from .models import Notes
from .models import Assignment
from .models import Response
from django.http import JsonResponse


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        # return render(request, 'html/assignment.html')
        return redirect('/assignment')


def loginUser(request):
    if request.method == "POST":
        usern = request.POST.get('username')
        userp = request.POST.get('password')
        user = authenticate(request, username=usern, password=userp)
        # print(usern,end="\n")
        # print(userp)
        if user:
            login(request, user)
            return redirect('/')
    else:
        return render(request,'html/login.html')
    return render(request,'html/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


def studentRegister(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name',"")
        email = form.get('email','')
        gender = form.get('gender','')
        class_stream = form.get('class_stream', '')
        class_year = form.get('class_year', '')
        mobile = form.get('mobile', '')
        password = form.get('password', '')
        confirm_password = form.get('confirm_password', '')

        if password == confirm_password and password != '':
            u = User.objects.create(username = email, email = email)
            u.set_password(password)
            u.save()

            s = Student()
            s.user = u
            s.email = u.email
            s.name = name
            s.class_stream = class_stream
            s.class_year = class_year
            s.mobile = mobile
            s.gender = gender
            s.save()
            
            return redirect('/login')
    return render(request, 'html/register.html')

    
@login_required(login_url='/login')
def addassignment(request, aid):
    # If user is staff redirect to assignment list.
    assignment = Assignment.objects.get(pk = aid)
    # If not assignment redirect to assignment lists 
    if request.method == 'POST':
        form = request.POST
        student = request.user.student
        aid = form.get("aId", "")
        assignment = Assignment.objects.get(pk = aid)
        assres = request.FILES.get('assres')
        print(student, aid, assignment, assres)
        if student and assignment :
            ar = AssignmentResponse.objects.create(student = student, assignment = assignment, assres = assres)
            return redirect("assignment")
    context = {
        'assignment' : assignment
    }
    return render(request, 'html/assignment.html', context)


def addassquestions(request):
    if not request.user.is_staff:
        return redirect("/")
    if request.method == "POST":
        if "Add" in request.POST:
            form= request.POST
            teacher = request.user
            q = form.get("q", '')
            cstream = form.get("class_stream", '')
            cyear = form.get("class_year", '')
            subject = form.get("Subject", '')

            if not "" in [cstream, q, subject, cyear]:
                quest = Assignment.objects.create(teacher = teacher, q = q, cstream = cstream, sub = subject, cyear = cyear)
                return redirect("/assignment")
    return render(request, "html/add-ass-question.html")


def assignment(request):
    questions = None
    if request.user.is_staff:
        questions = Assignment.objects.all()
    else:
        questions = Assignment.objects.all()
    
    context = {
        'questions' : questions
    }
    return render(request, "html/assignment-questions.html", context)


def assignmentresponse(request, aid):
    assignment = Assignment.objects.get(pk = aid)
    if assignment:
        ars = None
        if request.user.is_staff:
            ars = AssignmentResponse.objects.filter(assignment = assignment).all()
        else:
            ars = AssignmentResponse.objects.filter(assignment = assignment, student = request.user.student) 
        context = {
            'ars' : ars
        }
        print(ars)
        return render(request, "html/assignment-response.html", context)
    else:
        return redirect("assignment")


def deleteassignment(request, id):
    if not request.user.is_staff:
        return redirect("/")

    ar = AssignmentResponse.objects.get(pk=id)
    if not ar:
        return redirect("/addassignment")

    if ar:
        ar.delete()
    return redirect("/assignment")


def deleteassignmentq(request, id):
    if not request.user.is_staff:
        return redirect('/')
    
    aq = Assignment.objects.get(pk=id)
    if not aq:
        return redirect('/addassignment')

    if aq:
        aq.delete()
        return redirect('/assignment')


@require_http_methods(["GET"])
def get_questions(request):
    questions = Question.objects.all()
    data = [{'question': q.q, 'opt1': q.opt1, "opt2" : q.opt2, "opt3" : q.opt3, "opt4" : q.opt4, 'answer': q.ans} for q in questions]
    # return JsonResponse(data)
    return JsonResponse({'questions': data})


@login_required(login_url="/login/")
def showquestions(request):
    if not request.user.is_staff:
        return redirect("/")
    context = {
        'questions' : Question.objects.all()
    }
    return render(request, "html/showquestions.html", context)


def addquestion(request):
    if not request.user.is_staff:
        return redirect("/")
    if request.method == "POST":
        if "Add" in request.POST:
            form= request.POST
            q = form.get("q", '')
            o1 = form.get("o1", "")
            o2 = form.get('o2', '')
            o3 = form.get('o3', '')
            o4 = form.get('o4', '')
            choice = form.get('ans', '')

            ans = ''
            if choice == 'o1':
                ans = o1
            elif choice == 'o2':
                ans = o2
            elif choice == 'o3':
                ans = o3
            elif choice == 'o4':
                ans = o4
            
            if not "" in [q, o1, o2, o3, o4, ans]:
                quest = Question.objects.create(q = q, opt1 = o1, opt2 = o2, opt3 = o3, opt4 = o4, ans = ans)
                return redirect("showquestions")
    return render(request, "html/add-questions.html")


def exam(request):
    
    return render(request, "html/exam.html")


def submitresponse(request):
    pass


def updatequestion(request, qid):
    if not request.user.is_staff:
        return redirect("/")

    question = Question.objects.get(pk=qid)
    if not question:
        return redirect("/showquestions")
    if request.method == "POST":
        if "Update" in request.POST:
            form= request.POST
            q = form.get("q", '')
            o1 = form.get("o1", "")
            o2 = form.get('o2', '')
            o3 = form.get('o3', '')
            o4 = form.get('o4', '')
            choice = form.get('ans', '')

            ans = ''
            if choice == 'o1':
                ans = o1
            elif choice == 'o2':
                ans = o2
            elif choice == 'o3':
                ans = o3
            elif choice == 'o4':
                ans = o4
            
            if not "" in [q, o1, o2, o3, o4, ans]:
                question.q = q
                question.opt1 = o1
                question.opt2 = o2
                question.opt3 = o3
                question.opt4 = o4
                question.ans = ans
                question.save()
                return redirect("showquestions")
    context = {
        "question" : question
    }
    return render(request, "html/update-question.html", context)


def deletequestion(request, qid):
    if not request.user.is_staff:
        return redirect("/")

    question = Question.objects.get(pk=qid)
    if not question:
        return redirect("/showquestions")

    if question :
        question.delete()
    return redirect("showquestions")


@login_required(login_url='/login')
def notes(request):
    if request.method == "POST":
        form = request.POST
        cstream = form.get('class_stream','')
        cyear = form.get('class_year','')
        subject = form.get('subject_name','')
        subject_notes = request.FILES.get('subject_notes')
        if '' not in [cstream, cyear, subject]:
            n = Notes.objects.create(cstream = cstream, cyear = cyear, title = subject, notes = subject_notes)

            return redirect("/downloadnotes")
    return render(request, 'html/notes.html')


def downloadnotes(request):
    notes = Notes.objects.all()
    context = {
        'notes' : notes
    }
    return render(request, "html/download-notes.html", context)
    

def deletenotes(request, id):
    if not request.user.is_staff:
        return redirect("/")

    notes = Notes.objects.get(pk=id)
    if not notes:
        return redirect("/downloadnotes")

    if notes:
        notes.delete()
    return redirect("/downloadnotes")
    























