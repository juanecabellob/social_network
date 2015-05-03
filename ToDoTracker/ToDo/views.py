from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.core.urlresolvers import reverse
from .models import Poll, Choice, Todo
from django.views import generic
from django_ajax.decorators import ajax

class DetailsView(generic.DetailView):
    model = Poll
    template_name = 'ToDo/details.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'ToDo/results.html'

def vote(request, question_id):
    p = get_object_or_404(Poll, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'ToDo/details.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('ToDo:results', args=(p.id,)))

class IndexView(generic.ListView):
    template_name = 'ToDo/index.html'
    context_object_name = 'list_of_todos'

    def get_queryset(self):
        """Return the last five published questions."""
        return Todo.objects.order_by('-deadline')

def new(request):
    text = request.POST['text']
    deadline = request.POST['deadline']
    progress = request.POST['progress']
    newEntry = Todo(todo_text=text, deadline=deadline, progress=progress)
    newEntry.save()
    return HttpResponseRedirect(reverse('ToDo:index'))

def add(request):
    return render(request, 'ToDo/addTODO.html')
    # model = Poll

def about(request):
    return render(request, 'ToDo/impressum.html')

# Create your views here.

