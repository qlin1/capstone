from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'tool.html')

def result(request):
    context = {}
    return render(request, 'result.html')