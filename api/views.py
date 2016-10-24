from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.request import QueryDict
#from django.core.servers.basehttp import FileWrapper
from wsgiref.util import FileWrapper
from django.http import HttpResponse

from .models import Task
from .serializers import TaskSerializer
import json
import csv
import sys
import os

check = 'time'
alpha = 'abcdefghijklm'
NL = '\n'
PER = '.'
MODE = 'w+'
# Create your views here.
@api_view(['GET', 'POST'])
def task_list(request):
    debug("TEST")
    debug(os.path.dirname(os.path.abspath(__file__)))
    if request.method == 'GET':
        if len(request.query_params) > 0:
            print request.path
	    path_tail = request.path.split("/")[2]
	    final_filename = '../../protected/'+path_tail
	    ff = open(final_filename)
	    response = HttpResponse(FileWrapper(ff), content_type='application/csv')
	    response['Content-Disposition'] = 'attachment; filename="%s"' % path_tail
	    return response
        else:
            tasks = Task.objects.all()
            ser = TaskSerializer(tasks, many=True)
            return Response(ser.data)
    elif request.method == 'POST':
        path = "protected/"
        filename = request.data[0]["title"]
        sp = filename.split(PER)
        header = ','.join("{0}".format(k) for k in request.data[1].keys())
        content = header+NL
        content_length = 1
        index = 0
        for i in xrange(1, len(request.data)):
            line = ','.join("{0}".format(v) for (k,v) in request.data[i].items())
            if check in line:
                if content_length > 1:
                    final_filename = path+sp[0]+alpha[index]+PER+sp[1]
                    try:
                        with open(final_filename, MODE) as f:
                            content.encode('utf-8')
                            f.write(content)
                        content = line+NL
                        content_length = 1
                        index += 1
                    except IOError as e:
                        debug("IOError!!!!!")
                        debug(str(e))
            else:
                content += line+NL
                content_length += 1
            
        if content_length > 1:
            final_filename = path+sp[0]+alpha[index]+PER+sp[1]
            with open(final_filename, 'w') as f:
                content.encode('utf-8')
                f.write(content)
        
        if (len(request.data) > 0):
             return Response(request.data[0], status=status.HTTP_201_CREATED)

        else:
            return Response(
                request.data[0], status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method ==  'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        #task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def debug(obj):
    with open('debug/debug.txt', 'a') as f2:
        old_stdout = sys.stdout
        sys.stdout = f2
        print obj
        sys.stdout = old_stdout
