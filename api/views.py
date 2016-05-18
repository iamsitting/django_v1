from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.request import QueryDict

from .models import Task
from .serializers import TaskSerializer
import json
import csv
filename = '../sessionfiles/{0}_{1}_{2}-{3}.csv'

# Create your views here.
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        success = True
        #try:
        #    success = True
        #    dict_data = json.loads(posted_data)
        #    #print dict_data
        #except:
        #    success = False
        #    dict_data = request.data
        #    print 'failed json->dict conversion'
        
	print 'writing to file'
	final_filename = filename.format('05','16','16','1')
	with open(final_filename, 'w') as f:
		if success:
			for el in request.data:
				print el
				line = ','.join("{0}".format(v) for (k,v) in el.items())
				line.encode('utf-8')
				print line
				#for k in el.iterkeys():
				#	item = el[k].encode('utf-8')
				#	f.write(item+',')
				f.write(line+'\n')
		else:
			print "Handle this"
	print 'file written'
		#write to file

	
	#print posted_data
#        se = []
#        qdict = QueryDict('', mutable=True)
#        print dict_data[2]
#        for el in dict_data[1:]:
#            ts = TaskSerializer(data=qdict.update(el))
#            if ts.is_valid():
#                se.append(ts)
        #serializer = TaskSerializer(data=posted_data)
        #print se[1]
#        print len(se)
        if (len(request.data) > 0):
            return Response(request.data[0], status=status.HTTP_201_CREATED)
        #if serializer.is_valid():
            #serialzier.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
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
        
