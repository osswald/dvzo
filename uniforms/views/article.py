from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from uniforms.forms import CoatFieldsetForm
from uniforms.models import Article, CoatArticle


@method_decorator(login_required, name='dispatch')
class ArticleListView(generic.ListView):
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all()


@method_decorator(login_required, name='dispatch')
class CoatArticleCreateView(generic.CreateView):
    model = CoatArticle
    form_class = CoatFieldsetForm
    template_name = "uniforms/article_create_form.html"

    def form_valid(self, form):
        form.instance.category = "coat"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class CoatArticleUpdateView(generic.UpdateView):
    model = CoatArticle
    form_class = CoatFieldsetForm
    template_name = "uniforms/article_update_form.html"

    def get_success_url(self):
        return reverse_lazy("article-list")
