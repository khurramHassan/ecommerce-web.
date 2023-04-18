from django.http import HttpResponse

# Create your views here.

def view_home(request):
    return HttpResponse("<h1>welcome baham</h1>")
    
