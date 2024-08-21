from django.urls import path

from api_v1.views import calculate

app_name = 'api_v1'

urlpatterns = [
    path('<str:operation>/', calculate, name='calculate'),
]
