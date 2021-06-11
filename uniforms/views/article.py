from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from uniforms.forms import (CoatFieldsetForm, HatFieldsetForm, MiscFieldsetForm, ShirtFieldsetForm, ShoesFieldsetForm,
                            TieFieldsetForm, TrousersFieldsetForm, VestFieldsetForm)
from uniforms.models import (Article, CoatArticle, HatArticle, MiscArticle, ShirtArticle, ShoesArticle, TieArticle,
                             TrousersArticle, VestArticle)


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


@method_decorator(login_required, name='dispatch')
class HatArticleCreateView(generic.CreateView):
    model = HatArticle
    form_class = HatFieldsetForm
    template_name = "uniforms/article_create_form.html"

    def form_valid(self, form):
        form.instance.category = "hat"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class HatArticleUpdateView(generic.UpdateView):
    model = HatArticle
    form_class = HatFieldsetForm
    template_name = "uniforms/article_update_form.html"

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class MiscArticleCreateView(generic.CreateView):
    model = MiscArticle
    form_class = MiscFieldsetForm
    template_name = "uniforms/article_create_form.html"

    def form_valid(self, form):
        form.instance.category = "misc"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class MiscArticleUpdateView(generic.UpdateView):
    model = MiscArticle
    form_class = MiscFieldsetForm
    template_name = "uniforms/article_update_form.html"

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class ShirtArticleCreateView(generic.CreateView):
    model = ShirtArticle
    form_class = ShirtFieldsetForm
    template_name = "uniforms/article_create_form.html"

    def form_valid(self, form):
        form.instance.category = "shirt"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class ShirtArticleUpdateView(generic.UpdateView):
    model = ShirtArticle
    form_class = ShirtFieldsetForm
    template_name = "uniforms/article_update_form.html"

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class ShoesArticleCreateView(generic.CreateView):
    model = ShoesArticle
    form_class = ShoesFieldsetForm
    template_name = "uniforms/article_create_form.html"

    def form_valid(self, form):
        form.instance.category = "shoes"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class ShoesArticleUpdateView(generic.UpdateView):
    model = ShoesArticle
    form_class = ShoesFieldsetForm
    template_name = "uniforms/article_update_form.html"

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class TieArticleCreateView(generic.CreateView):
    model = TieArticle
    form_class = TieFieldsetForm
    template_name = "uniforms/article_create_form.html"

    def form_valid(self, form):
        form.instance.category = "tie"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class TieArticleUpdateView(generic.UpdateView):
    model = TieArticle
    form_class = TieFieldsetForm
    template_name = "uniforms/article_update_form.html"

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class TrousersArticleCreateView(generic.CreateView):
    model = TrousersArticle
    form_class = TrousersFieldsetForm
    template_name = "uniforms/article_create_form.html"

    def form_valid(self, form):
        form.instance.category = "trousers"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class TrousersArticleUpdateView(generic.UpdateView):
    model = TrousersArticle
    form_class = TrousersFieldsetForm
    template_name = "uniforms/article_update_form.html"

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class VestArticleCreateView(generic.CreateView):
    model = VestArticle
    form_class = VestFieldsetForm
    template_name = "uniforms/article_create_form.html"

    def form_valid(self, form):
        form.instance.category = "vest"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("article-list")


@method_decorator(login_required, name='dispatch')
class VestArticleUpdateView(generic.UpdateView):
    model = VestArticle
    form_class = VestFieldsetForm
    template_name = "uniforms/article_update_form.html"

    def get_success_url(self):
        return reverse_lazy("article-list")
