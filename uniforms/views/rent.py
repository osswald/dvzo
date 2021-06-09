from django.contrib.auth.decorators import login_required
from django.db.models import F, ExpressionWrapper, DecimalField
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from uniforms.forms import ArticleRentForm, RentForm
from uniforms.models import ArticleRent, Rent


@method_decorator(login_required, name='dispatch')
class RentListView(generic.ListView):
    context_object_name = "rents"

    def get_queryset(self):
        return Rent.objects.all()


@method_decorator(login_required, name='dispatch')
class RentDetailView(generic.DetailView):
    model = Rent
    template_name_suffix = "_detail_form"

    def get_context_data(self, **kwargs):
        article_rents = ArticleRent.objects.filter(rent=self.object)\
            .annotate(total_position=ExpressionWrapper(F('total_per_month') * F('rent__duration'),
                                                       output_field=DecimalField(max_digits=8, decimal_places=2)))
        return super().get_context_data(
            article_rents=article_rents,
            **kwargs)


@method_decorator(login_required, name='dispatch')
class RentUpdateView(generic.UpdateView):
    model = Rent
    form_class = RentForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("rent-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class RentCreateView(generic.CreateView):
    model = Rent
    form_class = RentForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("rent-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class RentDeleteView(generic.DeleteView):
    model = Rent
    template_name = "uniforms/confirm_delete.html"
    success_url = reverse_lazy("rent-list")


@method_decorator(login_required, name='dispatch')
class ArticleRentUpdateView(generic.UpdateView):
    model = ArticleRent
    form_class = ArticleRentForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("rent-detail", kwargs={'pk': self.object.rent.id})


@method_decorator(login_required, name='dispatch')
class ArticleRentCreateView(generic.CreateView):
    model = ArticleRent
    form_class = ArticleRentForm
    template_name_suffix = "_create_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.rent = get_object_or_404(Rent, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.rent = self.rent
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("rent-detail", kwargs={'pk': self.object.rent.id})


@method_decorator(login_required, name='dispatch')
class ArticleRentDeleteView(generic.DeleteView):
    model = ArticleRent

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("rent-detail", kwargs={'pk': self.object.rent.id})
