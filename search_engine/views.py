from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'search_engine/index.html'
    )