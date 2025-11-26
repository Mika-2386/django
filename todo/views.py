
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'index.html', {'list': todos, 'forms': form, 'title': 'Todo List'})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
    return redirect('index')

def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form, 'todo': todo})

def toggle_completed(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.completed = 'completed' in request.POST
        todo.save()
    return redirect('index')


