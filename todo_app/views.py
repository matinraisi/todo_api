from django.shortcuts import render , redirect ,get_object_or_404 
from .models import todo_list,category
from .form import todo_listForm
from django.views.generic.detail import DetailView

def home(request):
    query = todo_list.objects.all().order_by('created')


    form = todo_listForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = todo_listForm()
    context= {
        'query' : query,
        'form' : form,
    }
    return render(request, 'todo_app/index.html',context)


class TodoDetail(DetailView):
    model = todo_list
    template_name = 'todo_app/detail.html'


def delateTask(request,id):
    task = get_object_or_404(todo_list, id=id)
    task.delete()
    return redirect('home')