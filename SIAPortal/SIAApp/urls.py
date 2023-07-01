from django.contrib import admin
from django.urls import path, include
from SIAApp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),
    path('register', views.studentRegister, name='studentRegister'),

    path('notes', views.notes, name='notes'),
    path("downloadnotes", views.downloadnotes, name='downloadnotes'),
    path("deletenotes/<int:id>", views.deletenotes, name="deletenotes"),

    path('get_questions', views.get_questions, name='get_questions'),
    path("addquestion", views.addquestion, name='addquestion'),
    path("showquestions", views.showquestions, name='showquestions'),
    path("exam", views.exam, name='exam'),
    path("updatequestion/<int:qid>", views.updatequestion, name='updatequestion'),
    path("deletequestion/<int:qid>", views.deletequestion, name='deletequestion'),

    path("addassignment/<int:aid>", views.addassignment, name='addassignment'),
    path("assignment", views.assignment, name='assignment'),
    path("addassquestions", views.addassquestions, name="addassquestions"),
    path("assignmentresponse/<int:aid>", views.assignmentresponse, name="assignmentresponse"),
    path("deleteassignment/<int:id>", views.deleteassignment, name="deleteassignment"),
    path("deleteassignmentq/<int:id>", views.deleteassignmentq, name="deleteassignmentq"),
        
]


