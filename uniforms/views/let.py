from django.contrib.auth.decorators import login_required
from django.db.models import F, ExpressionWrapper, DecimalField
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from uniforms.forms import ArticleLetForm, LetForm
from uniforms.models import ArticleLet, Let


@method_decorator(login_required, name='dispatch')
class LetListView(generic.ListView):
    context_object_name = "lets"

    def get_queryset(self):
        return Let.objects.all()


@method_decorator(login_required, name='dispatch')
class LetDetailView(generic.DetailView):
    model = Let
    template_name_suffix = "_detail_form"

    def get_context_data(self, **kwargs):
        article_lets = ArticleLet.objects.filter(let=self.object)
        return super().get_context_data(
            article_lets=article_lets,
            **kwargs)


@method_decorator(login_required, name='dispatch')
class LetUpdateView(generic.UpdateView):
    model = Let
    form_class = LetForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("let-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class LetCreateView(generic.CreateView):
    model = Let
    form_class = LetForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("let-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class LetDeleteView(generic.DeleteView):
    model = Let
    template_name = "uniforms/confirm_delete.html"
    success_url = reverse_lazy("let-list")


@method_decorator(login_required, name='dispatch')
class ArticleLetUpdateView(generic.UpdateView):
    model = ArticleLet
    form_class = ArticleLetForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("let-detail", kwargs={'pk': self.object.let.id})


@method_decorator(login_required, name='dispatch')
class ArticleLetCreateView(generic.CreateView):
    model = ArticleLet
    form_class = ArticleLetForm
    template_name_suffix = "_create_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.let = get_object_or_404(Let, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.let = self.let
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("let-detail", kwargs={'pk': self.object.let.id})


@method_decorator(login_required, name='dispatch')
class ArticleLetDeleteView(generic.DeleteView):
    model = ArticleLet

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("let-detail", kwargs={'pk': self.object.let.id})
