from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Artikel


# Create your views here.
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
        print(kwargs)
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