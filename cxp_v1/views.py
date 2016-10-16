from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.utils.encoding import smart_str
from django.core.files import File
from wsgiref.util import FileWrapper
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from sendfile import sendfile
from .models import Download
import urllib
import os
import csv
import sys
import json
import mimetypes

#Class based views here

# Create your views here.
def foo(request):
    return render(request, 'cxp_v1/index.html')

@api_view(['GET'])
def dataplot(request):
    path = "./protected/"
    file_list = []
    for f in os.listdir(path):
        if 'csv' in f:
            file_list.append(f)
    context = {}
    if request.method == 'GET':
        debug(request.query_params)
        debug(len(request.query_params))
        if len(request.query_params) > 0:
            debug(request.query_params['downloadFile'])

            #Getting CSV data to plot
            if request.query_params['downloadFile'] == "no":
                debug('yes data')
                filename = request.query_params['filename']
                metric = request.query_params['metric']
                lab = getDataFromCSV(filename, 'time')
                dat = getDataFromCSV(filename, metric)
                context['stamps'] = lab
                context['raw_data'] = dat
                debug(context)
                return JsonResponse(context)
            else: #downloadFile yes
                debug("download file")
                debug(settings.SENDFILE_URL)
                debug(settings.SENDFILE_ROOT)
                return sendFile('10-13-2016-0.csv')
        else:

            debug('no data')
            context['filelist'] = file_list
            debug(context)
            return render_to_response('cxp_v1/dataplot.html', context)
    debug('end view')


def download(request, file_name):
    return sendFile(file_name)
@csrf_protect
def datasync(request):
    if request.method == 'POST':
        return HttpResponse("Thanks for POSTing.")
    else:
        return HttpResponse("No POST")

#defined non-view functions here
def getDataFromCSV(fname, label, toFloat=False):
    final_data = []
    filename = "./protected/"+fname
    with open(filename, 'rb') as f1:
        reader = csv.reader(f1)
        my_list = list(reader)
        
    index = my_list[0].index(label)
    
    if(toFloat):
        for sample in my_list[1:]:
            final_data.append(float(sample[index]))
    else:
        for sample in my_list[1:]:
            final_data.append(sample[index])
    
    return final_data

def sendFile(filename):
    path = "/home/ubuntu/Django/django_v1/protected/"+filename
    wrapper = FileWrapper(open(path))
    ctype, enc = mimetypes.guess_type(filename)
    if 'apk' in filename:
        ctype = 'application/vnd.android.package-archive'
    else:
        ctype = 'application/csv'
    response = HttpResponse(wrapper, content_type=ctype)
    response['Content-Length'] = os.path.getsize(path)
    response['Content-Disposition'] = "attachment; filename=%s"%filename
    debug(response)
    return response

#debug functions
def debug(obj):
    with open('debug/debug.txt', 'a') as f2:
        old_stdout = sys.stdout
        sys.stdout = f2
        print obj
        sys.stdout = old_stdout


