from django.contrib.auth.decorators import login_required
from django_tex.shortcuts import render_to_pdf

from train_management.models import DayPlanning


@login_required
def bulletin_pdf(request, pk):
    template_name = 'latex/bulletin.tex'
    dayplanning = DayPlanning.objects.get(pk=pk)
    context = {'dayplanning': dayplanning}
    return render_to_pdf(request, template_name, context, filename='briefing.pdf')
