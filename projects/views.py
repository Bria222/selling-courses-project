from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from .forms import ProjectForm

def home(request):
    project = Project.objects.all()
    context = {'project': project}
    return render(request, 'projects/home.html',context)

def contact(request):
    context = {}
    return render(request, 'projects/contact.html',context)

def about(request):
    project = Project.objects.all()
    context = {'project': project}
    return render(request, 'projects/about.html', context)


def projects(request):
    projectlist = Project.objects.all()
    context = {'projectlist': projectlist}
    return render(request, 'projects/projects.html', context)


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
       form = ProjectForm(request.POST,request.FILES)
       if form.is_valid():
          form.save()
          return redirect('home')

   

    context = {'form':form}
    return render(request, 'projects/project-form.html', context)



def updateProject(request):
    form = ProjectForm()