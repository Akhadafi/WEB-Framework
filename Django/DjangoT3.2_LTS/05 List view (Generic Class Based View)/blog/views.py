from django.shortcuts import render
from django.views.generic import ListView

from .models import Artikel


# Create your views here.
class ArtikelListView(ListView):
    model = Artikel
    # urut berdasarkan
    ordering = ["judul"]
    extra_context = {"judul": "Blog List"}

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        print(kwargs)
        return super().get_context_data(*args, **kwargs)


def index(request):
    context = {
        "judul": "Blog",
    }
    return render(request, "blog/index.html", context)
