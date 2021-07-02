from django.shortcuts import render,HttpResponse
from home.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home(request):
    context= {'success': False}
    if request.method =="POST":
        title =request.POST['title']
        desc = request.POST['desc']
        #print(title,desc)
        ins=Task(task_title=title,task_desc=desc)
        ins.save()
        context= {'success': True}
    return render (request,"index.html",context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks':allTasks
    }
    return render(request,"tasks.html",context)