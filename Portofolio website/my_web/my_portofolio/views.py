from django.shortcuts import render, redirect, get_object_or_404
from .forms import AboutMeForm, ContactForm, ProjectForm
from .models import AboutMe, Contact_model, Project_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import Project_model

def home_view(request):
    return render(request, 'home.html')

@login_required

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def about_me_edit_view(request):
    about_me = AboutMe.objects.first()
    if request.method == 'POST':
        form = AboutMeForm(request.POST, instance=about_me)
        if form.is_valid():
            form.save()
            return redirect('view_about_me')
    else:
        form = AboutMeForm(instance=about_me)
    return render(request, 'about_me_edit.html', {'form': form})



def view_about_me(request):
   
    about_me = AboutMe.objects.first()
    return render(request, 'view_about_me.html', {'about_me': about_me})



@login_required
def contact_edit_view(request):
    
    if not request.user.is_staff:
        return HttpResponseForbidden("Ju nuk keni qasje për të edituar këtë informacion.")

    contact = Contact_model.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('view_contact')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contact_edit.html', {'form': form})

def view_contact(request):
    
    contact = Contact_model.objects.first()
    return render(request, 'view_contact.html', {'contact': contact})

@login_required
def add_project_view(request):
    
    if not request.user.is_staff:
        return HttpResponseForbidden("Ju nuk keni qasje për të shtuar projekte.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

@login_required

def edit_project_view(request, pk):
    
    if not request.user.is_staff:
        return HttpResponseForbidden

    project = get_object_or_404(Project_model, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project_view(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden
    project = get_object_or_404(Project_model, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'delete_project.html', {'project': project})

def project_list_view(request):

    projects = Project_model.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project_model, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def project_list_view(request):
    projects = Project_model.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def upload_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')  
    else:
        form = ProjectForm()
    return render(request, 'upload_project.html', {'form': form})
