from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Log
from datetime import datetime
import json


# using this POST API to ingest the logs in the DB
@csrf_exempt
def ingest_logs(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_log = Log.objects.create(**data)
        return JsonResponse({'message': 'Log received and saved.'})
    return JsonResponse({'error': 'Invalid request.'}, status=400)


# GET API tp display web page to list all the logs that are ingestd
def display_logs(request):
    logs = Log.objects.all()
    return render(request, 'display_logs.html', {'logs': logs})


# Method to filter queries as per the requirements
def query_logs(request):
    trace_id = request.GET.get('traceId')
    level = request.GET.get('level')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    message = request.GET.get('message')
    resource_id = request.GET.get('resourceId')
    span_id = request.GET.get('spanId')
    commit = request.GET.get('commit')
    parent_resource_id = request.GET.get('metadata.parentResourceId')
    #print(start_date)
    logs = Log.objects.all()

    if trace_id:
        logs = logs.filter(traceId=trace_id)
    if level:
        logs = logs.filter(level=level)
    if message:
        logs = logs.filter(message__icontains=message)
        if "Failed to connect" in message and message is not None:
            logs = logs.filter(message__icontains="Failed to connect")
    if resource_id:
        logs = logs.filter(resourceId=resource_id)
    if span_id:
        logs = logs.filter(spanId=span_id)
    if commit:
        logs = logs.filter(commit=commit)
    if parent_resource_id:
        logs = logs.filter(metadata__parentResourceId=parent_resource_id)
    if start_date and not end_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M")
        logs = logs.filter(timestamp=start_date)

    if start_date and end_date:
        start_datetime = datetime.strptime(start_date, "%Y-%m-%dT%H:%M")
        end_datetime = datetime.strptime(end_date, "%Y-%m-%dT%H:%M")
        end_datetime = end_datetime.replace(hour=23, minute=59, second=59)  # Set the end time to the end of the day
        logs = logs.filter(timestamp__range=(start_datetime, end_datetime))


    if not any([trace_id, level, start_date,end_date,message, resource_id, span_id, commit, parent_resource_id]):
        logs = []

    return render(request, 'query_logs.html', {'logs': logs})
