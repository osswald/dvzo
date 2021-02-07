from django.shortcuts import render
from django_tex.shortcuts import render_to_pdf


def dashboard(request):
    return render(request, "train_management/dashboard.html")


def login(request):
    return render(request, "train_management/login.html")


def render_pdf(request):
    template_name = 'latex/test.tex'
    context = {'foo': 'Bar'}
    return render_to_pdf(request, template_name, context, filename='test.pdf')
