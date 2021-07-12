from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import do
from .form import myform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

class list(ListView):
    model = do
    template_name = 'index.html'
    context_object_name = 'obj'


class detail(DetailView):
    model = do
    template_name = 'detail.html'
    context_object_name = 'i'
class updatetask(UpdateView):
    model = do
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
class deletetask(DeleteView):
    model = do
    template_name = 'detele.html'
    success_url = reverse_lazy('list')


def index(request):
    obj = do.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        s = do(name=name, priority=priority, date=date)
        s.save()
    return render(request, 'index.html', {'obj': obj})


def delete(request, id):
    do1 = do.objects.get(id=id)
    if request.method == 'POST':
        do1.delete()
        return redirect('/')
    return render(request, 'detele.html', {'do1': do1})


def update(request, id):
    task = do.objects.get(id=id)
    form = myform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form})
