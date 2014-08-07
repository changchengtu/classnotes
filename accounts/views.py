from django.shortcuts import render
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect,HttpResponse
from notes.models import Note
from django.contrib.auth.decorators import login_required
import json


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")
    

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/shownotes/index")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def my_notes(request):
    data = {}
    data['id']=[]
    data['subject']=[]
    data['content']=[]
    username = None;
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    notes = Note.objects.filter(authors=username)
    for n in notes:
        data['id'].append(n.id)
        data['subject'].append(n.subject)
        data['content'].append(n.content)

    return HttpResponse(json.dumps(data), content_type="application/json")

