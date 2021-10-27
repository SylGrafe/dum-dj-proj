#"gettings started with django "detailed  comments 
# home/syl1/private/Pgm/djo1/top/polls/views_tut3.py
# the  corresponding file  used  in the django project  is
# home/syl1/private/Pgm/djo1/top/polls/views.py
# see also comments in   /home/syl1/private/Pgm/djo1/top/polls/urls_tut3.py

from django.http import HttpResponse
from django.template import loader
from .models import Question


# Create your views here.
'''
# example without using template
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
'''

'''
# example of using template and defining namespacing
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))    
'''





from django.shortcuts import render
# demo using the renderer shortcut instead loading template 
# and then sending hhtp response
'''
The render() function takes the request object as its first argument,
 a template name as its second argument 
 and a dictionary as its optional third argument.
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

'''    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
'''

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# demo raising a 404 error with  Http404
from django.http import Http404    
'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    
'''
    
from django.shortcuts import get_object_or_404, render

from .models import Question
# # demo using the  get_object_or_404 shortcut
'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})    

def detail(request, question_id):
    bar = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'foo': bar})    
'''

# test avec Daniel to notice the difference between the html varialbe and the 
# the pythonvariable

def detail(request, question_id):
    py_quest = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'temp_quest': py_quest})    

