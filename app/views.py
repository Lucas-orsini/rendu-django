from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from .models import Question
from .forms import QuestionForm

def index(request):
    context ={}
    context["dataset"] = Question.objects.all()

    return render(request,'app/index.html', context)

def create(request):
    context ={}
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app")

    context['form']= form
    return render(request, "app/create.html", context)

def details(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["data"] = Question.objects.get(id = id)

    return render(request, "app/details.html", context)

def update(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
    form = QuestionForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app/"+id)

    context["form"] = form
    return render(request, "app/update.html", context)

def delete(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/app")

    return render(request, "app/delete.html", context)


