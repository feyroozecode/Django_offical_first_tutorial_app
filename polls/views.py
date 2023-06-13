from django.http import HttpResponse 

def index(request):
    return HttpResponse("Alhamdoulillah, You'r at the polls index ")