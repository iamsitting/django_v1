from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse

# Create your views here.
def foo(request):
    return render(request, 'cxp_v1/index.html')

def dataplot(request):
    return render(request, 'cxp_v1/dataplot.html')

@csrf_protect
def datasync(request):
    if request.method == 'POST':
        return HttpResponse("Thanks for POSTing.")
    else:
        return HttpResponse("No POST")
