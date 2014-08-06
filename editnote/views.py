from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from notes.models import Note
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return render(request,'editnote/index.html')

def save(request):
	print request.POST
	n = Note(subject=request.POST.get('subject'),content=request.POST.get('editor'))
	n.save()
	return HttpResponseRedirect('/shownotes/index')

	
	
