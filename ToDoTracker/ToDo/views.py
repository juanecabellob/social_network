from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Todo
from django.views import generic
from django_ajax.decorators import ajax

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

@ajax
def edit(request):
    p = get_object_or_404(Todo, pk=request.POST['id'])
    p.todo_text = request.POST['text']
    p.deadline = request.POST['deadline']
    p.progress = request.POST.get('progress', '0%')
    p.save()
    return {p.todo_text}

@ajax
def delete(request):
    p = get_object_or_404(Todo, pk=request.POST['id'])
    p.delete()
    return "Succeed"
# Create your views here.

