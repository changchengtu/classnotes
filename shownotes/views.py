from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from notes.models import Note
import json
from django.views.decorators.csrf import csrf_protect

def index(request):
	username = None

	note = Note.objects.all()[:10]
	if request.user.is_authenticated():
		username = request.user.username
	else:
		username = None


	context = RequestContext(request, {
        'note': note,
        'username': username,
    })

	return render(request, 'shownotes/index.html', context)

def getContent(request):

	data = {}
	pk = request.GET.get('q','')

	note = Note.objects.get(id=pk)
	data['school_name'] = note.school_name
	data['department_name'] = note.department_name
	data['class_name'] = note.class_name
	data['subject'] = note.subject
	data['content'] = note.content
	print 'getContent'
	return HttpResponse(json.dumps(data), content_type="application/json")

def getNoteList(request):
	data = {}
	data['id']=[]
	data['subject']=[]
	data['content']=[]

	school_name = request.GET.get('s','')
	department_name = request.GET.get('d','')
	notes = Note.objects.filter(school_name=school_name,department_name=department_name)
	for n in notes:
		data['id'].append(n.id)
		data['subject'].append(n.subject)
		data['content'].append(n.content)
		
	return HttpResponse(json.dumps(data), content_type="application/json")

def getSchoolList(request):

	data = {}
	notes = Note.objects.all()
	school_list=[]
	for note in notes:
		school_list.append(note.school_name)
	data['content'] = list(set(school_list))
	print "getSchoolList"
	return HttpResponse(json.dumps(data), content_type="application/json")


def getDepartmentList(request):

	data = {}
	notes = Note.objects.all()
	department_list=[]
	for note in notes:
		department_list.append(note.department_name)
	data['content'] = list(set(department_list))
	print "getDepartmentList"
	return HttpResponse(json.dumps(data), content_type="application/json")

