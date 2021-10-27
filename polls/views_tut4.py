# home/syl1/private/Pgm/djo1/top/polls/views_tut4.py
# covers also tutorial4 upp to but not including  generic views
# https://docs.djangoproject.com/en/3.1/intro/tutorial04/
# for more comments , "gettings started with django detailed  comments" see 
# home/syl1/private/Pgm/djo1/top/polls/views_tut3.py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})    


'''
request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # selected_choice comes from the template
        # /home/syl1/private/Pgm/djo1/top/polls/templates/polls/detail.html  
        # <form action="{% url 'polls:vote' question.id %}" method="post">
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


'''
We are using the reverse() function in the HttpResponseRedirect constructor in this example. This function helps avoid having to hardcode a URL in the view function. It is given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view. In this case, using the URLconf we set up in Tutorial 3, this reverse() call will return a string like

'/polls/3/results/'
where the 3 is the value of question.id. This redirected URL will then call the 'results' view to display the final page.
'''
    

'''
more info about reverse in
/home/syl1/private/Pgm/djo1/lathundDjango.txt
'''