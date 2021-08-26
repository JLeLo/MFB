# from django.contrib.auth import User
from rest_framework import routers, serializers, viewsets

from django.db import models
# Serializers define the API representation.


class ChecklistSerializer(serializers.Serializer):
    check_name = serializers.CharField(max_length=100)
    check_details = serializers.CharField(max_length=100)
    check_vuln_root_cause = serializers.CharField(max_length=100)
    check_remediation = serializers.CharField(max_length=100)
    check_tags = serializers.CharField(max_length=100)
    check_patch_references = serializers.CharField(max_length=100)
    check_exploit_references = serializers.CharField(max_length=100)


class ProjectSerializer(serializers.Serializer):
    project_name = serializers.CharField(
        max_length=100)     # name of column 2
# how to define date in django modules
    project_date_created = serializers.DateField()
    project_date_last_executed = serializers.DateField()
    project_status_list = (
        ('NOT STARTED', 'The project is not yet started'),
        ('RUNNING', 'The project is running now'),
        ('STOPPED', 'The was running earlier, but now it is stopped'),
        ('COMPLETED', 'The project has finished execution')
    )

    project_status = serializers.CharField(
        max_length=50, default='NOT STARTED')

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
