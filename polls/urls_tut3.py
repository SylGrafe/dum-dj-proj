# "gettings started with django "detailed  comments 
# this file is  /home/syl1/private/Pgm/djo1/top/polls/urls_tut3.py
# the  corresponding file  used  in the django project  is
# /home/syl1/private/Pgm/djo1/top/polls/urls.py
# covers also tutorial4 upp to but not including  generic views

# https://docs.djangoproject.com/en/3.1/intro/tutorial03/
# # https://docs.djangoproject.com/en/3.1/topics/http/urls/#term-application-namespace
from django.urls import path
from . import views
app_name = 'polls'


'''
   relation between urls.py , view.py index.html and detail.html
   notice that the html files are under the subfolder  .../polls/templates/polls/...

   in    /home/syl1/private/Pgm/djo1/top/polls/urls_tut3.py look at   
   path('<int:question_id>/', views.detail, name='detailXX'),

   path('<int:question_id>/', views.detail,
   makes the link between http://127.0.0.1:8000/polls/1/ 
   and  de details function in 
   home/syl1/private/Pgm/djo1/top/polls/views.py defined by 
   
   
    def detail(request, question_id):
    py_quest = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'temp_quest': py_quest})    

    render(request, 'polls/detailXX.html',  return statement 
    inform django to  get this page in the browser:
    /home/syl1/private/Pgm/djo1/top/polls/templates/polls/detail.html  

    because detailXX is define in index_tut3.html
    /home/syl1/private/Pgm/djo1/top/polls/templates/polls/index_tut3.html
    <li> <a href="{% url 'polls:detailXX' question.id %}">{{ question.question_text }}

'''



urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detailXX'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


# https://docs.djangoproject.com/en/3.1/ref/urls/
# path(route, view, kwargs=None, name=None)

# root argument
'''
The route argument should be a string or gettext_lazy() (see Translating URL patterns) that contains a URL pattern. 
The string may contain angle brackets (like <username> above) to capture part of the URL and send it as a keyword argument to the view. The angle brackets may include a converter specification (like the int part of <int:section>) which limits the characters matched and may also change the type of the variable passed to the view. For example, <int:section> matches a string of decimal digits and converts the value to an int. See How Django processes a request for more details.
'''
# The view argument
'''
The view argument is a view function or the result of as_view() for class-based views. It can also be an django.urls.include().
in     path('', views.index, name='index'),
views.index refers to  index function defined in the python file
home/syl1/private/Pgm/djo1/top/polls/views.py

'''
# name=None argument
'''
https://docs.djangoproject.com/en/3.1/topics/http/urls/#naming-url-patterns
Naming URL patterns
In order to perform URL reversing, you’ll need to use named URL patterns as done in the examples above. The string used for the URL name can contain any characters you like. You are not restricted to valid Python names.

((illustration for name= see detailXX in ))
file /home/syl1/private/Pgm/djo1/top/polls/templates/polls/index.html
....
        <li> <a href="{% url 'polls:detailXX' question.id %}">{{ question.question_text }}

((related use of detailXX in ))
file /home/syl1/private/Pgm/djo1/top/polls/urls.py
...
    path('<int:question_id>/', views.detail, name='detailXX'),






'''

