from django.http import HttpResponse 

def index(request):
    return HttpResponse("Alhamdoulillah, You'r at the polls index ")

def detail(request, question_id):
    return HttpResponse('You\'re looking at question %s.'
                         % question_id)

def results(request, question_id):
    response = 'You\re looking results of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You\'re looking voting on question %s' 
                        %question_id)

