
from django.http.response import HttpResponse
from django.urls import path

def Home(request):

    return HttpResponse("home in core")

urlpatterns = [
    path('test/', Home),
]
