# home/syl1/private/Pgm/djo1/top/polls/views.py
# covers generic views from tutorial4
# https://docs.djangoproject.com/en/3.1/intro/tutorial04/
# for more comments , "gettings started with django detailed  comments" see 
# home/syl1/private/Pgm/djo1/top/polls/views_tut3.py
# home/syl1/private/Pgm/djo1/top/polls/views_tut4.py

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Choice, Question

'''
We’re using two generic views here: ListView and DetailView. Respectively, those two views abstract the concepts of “display a list of objects” and “display a detail page for a particular type of object.”
'''
'''
about context_object_name
In previous parts of the tutorial, the templates have been provided with a context that contains the question and latest_question_list context variables. For DetailView the question variable is provided automatically – since we’re using a Django model (Question), Django is able to determine an appropriate name for the context variable. However, for ListView, the automatically generated context variable is question_list. To override this we provide the context_object_name attribute, specifying that we want to use latest_question_list instead.
'''




class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions but not those pubished in the 
         future
         ."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
        pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


'''
about template_name = 
By default, the DetailView generic view uses a template called
 <app name>/<model name>_detail.html. In our case, it would use the template "polls/question_detail.html"
'''

'''
about model=
Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views.
'''

# test 20201216 for Daniel , usign get_context_data()
from django.utils import timezone
import random

class DetailView( SuccessMessageMixin, generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    # 20201216 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['someInt'] = random.randint(0,999)
        return context


    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# vote same as before
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    someMessage = "here in DetailView note()"
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # selected_choice comes from the template
        # /home/syl1/private/Pgm/djo1/top/polls/templates/polls/detail.html  
        # <form action="{% url 'polls:vote' question.id %}" method="post">
        someMessage = "here in DetailView note() some success message"
        messages.success(request,  (someMessage))

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        someMessage = "here in DetailView note() some failure message"
        messages.error(request,  (someMessage))

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



