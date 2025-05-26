from django.shortcuts import render,redirect
# filepath: views.py
from .models import Task
from .forms import TodoForm
#from django.views.generic import ListView 

def index(request):
  task_list = Task.objects.all()
  if request.method == 'POST':
    name = request.POST.get('name','')
    priority = request.POST.get('priority','')
    date = request.POST.get('date','')
    task = Task(name=name, date=date, priority=priority)
    task.save()
    return redirect('/')
    #task.clear()
  return render(request,'html/index.html',{'task_list':task_list})
  task.clear()
  
  # ...existing code...
def delete(request, task_id):
    task = Task.objects.get(id=task_id)  # or pk=task_id if your model uses 'pk'
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'html/delete.html', {'task': task})
# ...existing code...
def update(request, task_id):
  task = Task.objects.get(id=task_id)
  form = TodoForm(request.POST or None, instance=task)
  if form.is_valid():
    form.save()
    return redirect('/') 
  return render(request, 'html/Edit.html', {'form': form, 'task': task})
  