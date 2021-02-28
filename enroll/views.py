from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from .models import Student
from django.views.generic.base import TemplateView

# Create your views here.
class StudentCreateview(CreateView):
    model = Student
    fields=['name','roll','email']
    success_url='thanks'

class ThanksTemplateView(TemplateView):
    template_name='enroll/createthanks.html'

class StudentUpdateview(UpdateView):
    model=Student
    fields=['name','roll','email']
    success_url='/updatethanks/'


class UpdateThanksTemplateView(TemplateView):
    template_name='enroll/updatethanks.html'
