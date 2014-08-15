from django.shortcuts import render
from django.http import HttpResponse
from progress.models import *

# Create your views here.
def index(request):

	curriculum_list = Curriculum.objects.all().values('id','name')
	print curriculum_list.count
	context = {'curriculum_list':curriculum_list}
	return render(request,'index.html',context)
	