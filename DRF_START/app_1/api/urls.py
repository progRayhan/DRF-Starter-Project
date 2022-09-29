from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Fuck You !")

urlpatterns = [
    path('', home, name="home"),
]