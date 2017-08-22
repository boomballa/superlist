from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"Hello Shiyanlou!")

def home(request):
#    string = u"Shiyanlou is very good!"
    TutorialList = ["HTML","CSS","jQuery","Python","Django"]
    return render(request, 'home.html', {'TutorialList': TutorialList})