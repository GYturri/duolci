from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import CaidoForm

from .models import Caidos

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Caidos()
    greeting.save()

    greetings = Caidos.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

class Reg(CreateView):
    template_name = "index.html"
    form_class = CaidoForm
    success_url = '/error'
    def form_valid(self, form):
        return super(Reg, self).form_valid(form)
    def form_invalid(self, form):
        return super(Reg, self).form_invalid(form)

class Mierror(TemplateView):
    template_name = "error.html"