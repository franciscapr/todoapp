from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.

# Creación de tareas
def createTodoView(request):
    form = TodoForm
    if request.method == 'POST':     
        form = TodoForm(request.POST)
        if form.is_valid():    # Validamos los datos del form
            form.save()    # Guardamos el nuevo elemento si es valido
            return redirect('show_url')    # Redireccionamos
    template_name = 'todoapp/todo.html'    # Pasamos el objeto form en el context
    context = {'form': form}
    return render(request, template_name, context)
    
    
# Mostrar todo
def showTodoView(request):
    obj = Todo.objects.all()
    template_name = 'todoapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)


# Update View
def updateTodoView(request, f_id):
    obj =Todo.objects.get(id=f_id)
    form = TodoForm(instance=obj)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'todoapp/todo.html'
    context = {'form': form}
    return render(request, template_name, context)

    
# Delete View
def deleteTodoView(request, f_id):
    obj = Todo.objects.get(id=f_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'todoapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)