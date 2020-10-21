from django.urls import path
from api import views

app_name='api'

urlpatterns=[
    path('',views.UserAPIView.as_view(),name='users'),
    path('activity_period/',views.ActivityPeriodAPIView.as_view(),name='activity_period'),
    path('getFromJson/',views.getFromJson,name="getFromJson")
]