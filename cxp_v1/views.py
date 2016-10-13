from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from sendfile import sendfile
from .models import Download
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
    path = "../sessionfiles/"
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
            if request.query_params['downloadFile'] == "no":
                debug('yes data')
                filename = request.query_params['filename']
                metric = request.query_params['metric']
                lab = getDataFromCSV(filename, 'time')
                dat = getDataFromCSV(filename, metric)
                lab_json = json.dumps(lab, cls=DjangoJSONEncoder)
                dat_json = json.dumps(dat, cls=DjangoJSONEncoder)
                context['stamps'] = lab #lab_json
                context['csv_data'] = dat #dat_json
                debug(context)
                return JsonResponse(context)
                return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), content_type = "application/json")
            else: #downloadFile yes
                debug("download file")
                debug(request.query_params['filename'])
                return sendFile('07-09-2016-6.csv')
                #fpath = "/home/ubuntu/Django/sessionfiles/protected/07-09-2016-6.csv"
                #debug("fpath: "+fpath)
                #with open(fpath, 'rb') as fh:
                #    response = HttpResponse(fh.read(), content_type="text/csv")
                #    response['Content-Disposition'] = 'attachment; filename="07-09-2016.csv"'
                #    return response
                #return sendfile(request, path, attachment=True)


        else:

            debug('no data')
            context['filelist'] = file_list
            debug(context)
            return render_to_response('cxp_v1/dataplot.html', context)
    debug('end view')
    #return render_to_response('cxp_v1/dataplot.html', {'filelist':file_list,
    #                                                    'stamps':lab_json,
    #                                                    'csv_data':dat_json})
    #return render_to_response('cxp_v1/dataplot.html', context)
    #return render(request, 'cxp_v1/dataplot.html')

@api_view(['GET'])
def download(request, download_id):
    download = get_object_or_404(Download, pk=download_id)
    if(True):
    #if(download_id == 'cxp-apk'):
        debug("GET download")
        return sendfile(request, download.file.path)

@csrf_protect
def datasync(request):
    if request.method == 'POST':
        return HttpResponse("Thanks for POSTing.")
    else:
        return HttpResponse("No POST")

#defined non-view functions here
def getDataFromCSV(fname, label, toFloat=False):
    final_data = []
    filename = "../sessionfiles/"+fname
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
    path = "/home/ubuntu/Django/sessionfiles/protected/"+filename
    dl_name = "sample.csv"
    wrapper = FileWrapper(open(path))
    ctype, enc = mimetypes.guess_type(filename)
    if ctype is None:
        ctype = 'application/octet-stream'
    #response = HttpResponse(wrapper, content_type=ctype)
    response = StreamingHttpResponse(wrapper, content_type = ctype)
    response['Content-Length'] = os.path.getsize(path)
    response['Content-Disposition'] = "attachment; filename=%s"%dl_name
    return response

#defbug functions
def debug(obj):
    with open('../debug/debug.txt', 'a') as f2:
        old_stdout = sys.stdout
        sys.stdout = f2
        print obj
        sys.stdout = old_stdout


