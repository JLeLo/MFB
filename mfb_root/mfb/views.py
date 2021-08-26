from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import path
from .models import checklists, projects
from .serializers import ChecklistSerializer, ProjectSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def fetch_checks(request, pk):
    check_data = checklists.objects.get(id=pk)
    serializer_data = ChecklistSerializer(check_data)
    # json_data = JSONRenderer().render(serializer_data.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer_data.data)


def all_checks(request):
    check_data = checklists.objects.all()
    serializer_data = ChecklistSerializer(check_data, many=True)
    # json_data = JSONRenderer().render(serializer_data.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer_data.data, safe=False)


def all_projects(request):
    check_data = projects.objects.all()
    serializer_data = ProjectSerializer(check_data, many=True)
    return JsonResponse(serializer_data.data, safe=False)


def index(request):
    # this will by default search in app/templates folder.
    return render(request, 'index.html')
