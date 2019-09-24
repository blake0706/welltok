from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from welltokapi.serializers import TopicSerializer
from django.contrib.auth.models import User
from topics.models import Topic

# Create your views here.

# ViewSets define the view behavior.
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
