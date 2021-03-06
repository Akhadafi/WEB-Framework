from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView

from .forms import ArtikelForm
from .models import Artikel


class ArtikelCreateView2(CreateView):
    model = Artikel
    fields = [
        "judul",
        "isi",
        "penulis",
    ]
    # template akan di ambil dari artikel_form, suffix_form
    extra_context = {
        "judul": "Tambah Artikel dengan create view 2",
    }

    def get_context_date(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)


class ArtikelCreateView1(CreateView):
    form_class = ArtikelForm
    template_name = "blog/create.html"

    extra_context = {
        "judul": "Tambah Artikel dengan create view 1",
    }

    def get_context_date(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)


# Create your views here.
class ArtikelFormView(FormView):
    form_class = ArtikelForm
    template_name = "blog/create.html"
    success_url = reverse_lazy("blog:list", kwargs={"penulis": "all"})
    extra_context = {
        "judul": "Tambah Artikel",
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def form_valid(self, form):
        # print(form.cleaned_data)
        form.save()
        return super().form_valid(form)


class ArtikelDetailView(DetailView):
    model = Artikel
    extra_context = {
        "judul": "Detail Artikel",
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        artikel_lain = self.model.objects.exclude(slug=self.kwargs["slug"])
        self.kwargs.update({"artikel_lain": artikel_lain})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class ArtikelListView(ListView):
    model = Artikel
    # urut berdasarkan
    ordering = ["judul"]
    # membagi halaman
    # paginate_by = 2
    extra_context = {
        "judul": "Blog List",
    }

    def get_queryset(self):
        if self.kwargs["penulis"] != "all":
            self.queryset = self.model.objects.filter(
                penulis__iexact=self.kwargs["penulis"]
            )
            self.kwargs.update(
                {
                    "punulis": self.kwargs["penulis"],
                }
            )
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        print(kwargs)
        return super().get_context_data(*args, **kwargs)
