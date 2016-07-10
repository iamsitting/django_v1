from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
import os

# Create your views here.
def foo(request):
    return render(request, 'cxp_v1/index.html')

def dataplot(request):
    path = "../sessionfiles/"
    file_list = os.listdir(path)
    print file_list
    return render_to_response('cxp_v1/dataplot.html', {'filelist':file_list})
    #return render(request, 'cxp_v1/dataplot.html')

@csrf_protect
def datasync(request):
    if request.method == 'POST':
        return HttpResponse("Thanks for POSTing.")
    else:
        return HttpResponse("No POST")
