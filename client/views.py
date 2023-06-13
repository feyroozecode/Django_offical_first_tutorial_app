from django.shortcuts import render
from polls.models import Question

# Create your views here.

def index(request): 
    # retrieves all questions
    questions = Question.objects.all()

    # Pass the questions to the template 
    context = {
        'questions': questions
    } 

    return render(request, 'client/index.html', context)