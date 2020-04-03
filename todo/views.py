from django.shortcuts import render,redirect
from .models import todo
from .forms import todoform
from django.views.decorators.http import require_POST

def index(request):
    todo_list = todo.objects.order_by('id')
    form = todoform()
    context = {'todo_list': todo_list, 'form' : form}
    return render(request,'todo/index.html',context)

@require_POST
def addtodo(request):
    form= todoform(request.POST)
    print(request.POST['text'])

    if form.is_valid():
        new_todo = todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completedtodo(request,todo_id):
    to_do = todo.objects.get(pk=todo_id)
    to_do.complete = True
    to_do.save()
    return redirect('index')

def deletecompleted(request):
    todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteall(request):
    todo.objects.all().delete()
    return redirect('index')