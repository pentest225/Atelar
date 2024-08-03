from django.shortcuts import render


# Create your views here.
def index(request):
    print("On The Index Page")
    return render(request, 'index4.html')
