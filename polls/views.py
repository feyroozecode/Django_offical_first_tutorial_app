from django.shortcuts import render, get_object_or_404
from .models import Question

"""
    Index View:
        Displays the latest questions on a webpage.
    Parameters:
        - request (HttpRequest): The HTTP request object.
    Returns:
        - HttpResponse: The HTTP response containing the rendered template with the latest questions.
    
 """
def index(request):
    # get all question ordered by pub date and get the latest 5 question
    latest_question_list = Question.objects.order_by('-pub_date') [:5]
    context = {"latest_question_list": latest_question_list}
    # return the response
    return render(request, "polls/index.html", context)

"""
    - Detail View:
        Displays the details of a specific question.
    Parameters:
        - request (HttpRequest): The HTTP request object.
        - question_id (int): The ID of the question to display.
    Returns:
    - HttpResponse: The HTTP response containing the details of the specified question.
    
    TryCatch : 
        Handle the good response and 404 Found if Question does not exist
 """
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = 'You\re looking results of question %s.'
    return render(request, "polls/results.html", {"results": response % question_id})

"""
    Vote View:
     - Handles the voting on a specific question.
    Parameters:
        - request (HttpRequest): The HTTP request object.
        - question_id (int): The ID of the question to vote on.
    Returns:
    - HttpResponse: The HTTP response indicating the voting action on the specified question.
"""
def vote(request, question_id):
    return HttpResponse('You\'re looking voting on question %s' 
                        %question_id)

