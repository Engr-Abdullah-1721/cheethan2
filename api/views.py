from django.shortcuts import render
from api import models
from api.serializers import UserSerializer,ActivityPeriodSerializer
from rest_framework.generics import ListCreateAPIView
import json
from django.http import JsonResponse
# Create your views here.

class UserAPIView(ListCreateAPIView):
    serializer_class=UserSerializer
    queryset=models.User.objects.all()


class ActivityPeriodAPIView(ListCreateAPIView):
    serializer_class=ActivityPeriodSerializer
    queryset=models.ActivityPeriod.objects.all()


from django.utils.dateparse import parse_date
import datetime
def getFromJson(request):
    users=models.User.objects.all()
    names=[]
    for user in users:
        names.append(user.real_name)
    data=open('static/eg.json').read()
    jsonData=json.loads(data)
    for member in jsonData['members']:
        if member['real_name'] not in names:
            user1=models.User.objects.create(real_name=member['real_name'],tz=member['tz'])
            for activity in member['activity_periods']:
                a=activity['start_time'].split(' ')
                print(a)
                
                print('start_time',activity['start_time'],' ------------end_time',activity['end_time'])
                models.ActivityPeriod.objects.create(user=user1,start_time=activity['start_time'],end_time=activity['end_time'])
    return JsonResponse({'ok':jsonData})