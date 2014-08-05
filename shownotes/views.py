from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from notes.models import Note
import json
from django.views.decorators.csrf import csrf_protect

def index(request):
	note = Note.objects.all()[:10]
	context = RequestContext(request, {
        'note': note,
    })

	return render(request, 'shownotes/index.html', context)

def getContent(request):

	data = {}
	pk = request.GET.get('q','')

	note = Note.objects.get(id=pk)
	data['content'] = note.content
	print note.content
	return HttpResponse(json.dumps(data), content_type="application/json")

