from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import *

from . forms import CalcForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def prepara_dati():

    # model_instance._meta.db_table
    # Elimina tutto 
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('DELETE FROM polls_Coso')
    cursor.execute('DELETE FROM polls_AttributoCoso')

    # Inserisci
    c1 = Coso()
    c1.id_coso = 1
    c1.descrizione_coso = "Coso N° 1"
    c1.save()

    a=None
    a=AttributoCoso()
    a.id_coso=c1
    a.cod_attributo="A"
    a.valore_attributo="1 -- attr A"
    a.save()

    a=None
    a=AttributoCoso()
    a.id_coso=c1
    a.cod_attributo="B"
    a.valore_attributo="1 -- attr B"
    a.save()

    a=None
    a=AttributoCoso()
    a.id_coso=c1
    a.cod_attributo="C"
    a.valore_attributo="1 -- attr C"
    a.save()

    c2 = Coso()
    c2.id_coso = 2
    c2.descrizione_coso = "Coso N° 2"
    c2.save()

    # Riscrivo il 2
    c2b = Coso()
    c2b.id_coso = 2 # Volutament ancora 2
    c2b.descrizione_coso = "Coso N° 2 riscritto"
    c2b.save()

    a=None
    a=AttributoCoso()
    a.id_coso=c2
    a.cod_attributo="A"
    a.valore_attributo="2 -- attr A"
    a.save()

    a=None
    a=AttributoCoso()
    a.id_coso=c2
    a.cod_attributo="B"
    a.valore_attributo="2 -- attr B"
    a.save()

    a=None
    a=AttributoCoso()
    a.id_coso=c2
    a.cod_attributo="C"
    a.valore_attributo="2 -- attr C"
    a.save()

    c3 = Coso()
    c3.id_coso = 3
    c3.descrizione_coso = "Coso N° tre"
    c3.save()                

    cx = Coso.objects.get(id_coso=3)
    cx.descrizione_coso = "Coso N° 3"
    cx.save()

    # 

def test(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/test.html')

    prepara_dati()
 

    cosi = Coso.objects.all()

    context = {
        'titolo': "Test modelli",
        'cosi' : cosi,
    }
    # debug-only: print (template.render(context, request))
    return HttpResponse(template.render(context, request))



def calc(request):
    template_file = 'polls/calc.html'


    x = 0
    y = 0
    ris = 0    
    if request.method == "POST":
        calc_form = CalcForm(request.POST)
        if calc_form.is_valid():

            x = calc_form.cleaned_data["x"]
            y = calc_form.cleaned_data["y"]

            try:
                ris = float(x) + float(y)
            except:
                ris = "errore"    
    else:
        calc_form = CalcForm()            

    context = {
        'form' : calc_form,
        'ris' : ris,        
    }
    
    return render(request, template_file, context)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     print (template.render(context, request))
#     return HttpResponse(template.render(context, request))
#     
# def detail(request, question_id): 
#     q = Question.objects.get(id=question_id)
#     context = {
#         "question" :  q 
#     }
#     detail_template = loader.get_template('polls/detail.html')
#     return HttpResponse(detail_template.render(context, request))
#     # return HttpResponse("You're looking at question %s." % detail) 
# 
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
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