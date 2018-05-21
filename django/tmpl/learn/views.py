from django.shortcuts import render

def home(request):
    TutorialList = ["HTML","CSS","JQUERY","Python","Django"]
    return render(request,'home.html',{'TutorialList':TutorialList})
    